import pytest
from conversation import Conversation, Artifact, Tool
import json
import tempfile
import os

def test_artifact_str():
    artifact = Artifact("18bacG4a", "text/markdown", "Test Title", "Test Content")
    expected = '<artifact identifier="18bacG4a" type="text/markdown" title="Test Title">\nTest Content\n</artifact>'
    assert str(artifact) == expected

def test_conversation_initialization():
    conv = Conversation()
    assert conv.messages == []
    assert conv.tools == []
    assert conv.filename is None

def test_conversation_with_file():
    # Create a temporary file with test messages
    test_messages = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there"}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
        json.dump(test_messages, tf)
        temp_filename = tf.name
    
    try:
        # Test loading existing file
        conv = Conversation(filename=temp_filename)
        assert conv.messages == test_messages
        
        # Test saving messages
        new_message = {"role": "user", "content": "How are you?"}
        conv.messages.append(new_message)
        conv._save()
        
        # Verify save worked
        with open(temp_filename, 'r') as f:
            saved_messages = json.load(f)
        assert len(saved_messages) == 3
        assert saved_messages[-1] == new_message
    
    finally:
        # Cleanup
        os.unlink(temp_filename)

def test_conversation_nonexistent_file():
    conv = Conversation(filename="nonexistent.json")
    assert conv.messages == []

def test_tool_initialization():
    schema = {
        "name": "test_tool",
        "description": "A test tool"
    }
    def dummy_callable(input):
        return f"Processed: {input}"
    
    tool = Tool(schema, dummy_callable)
    assert tool.name == "test_tool"
    assert tool.schema == schema
    assert tool.callable("test") == "Processed: test"

def test_process_tool_call():
    def dummy_tool(input):
        return f"Processed: {input}"
    
    tool = Tool({"name": "test_tool"}, dummy_tool)
    conv = Conversation(tools=[tool])
    
    result = conv._process_tool_call("test_tool", "test input")
    assert result == "Processed: test input"
    
    with pytest.raises(Exception) as exc_info:
        conv._process_tool_call("nonexistent_tool", "test input")
    assert str(exc_info.value) == "Tool nonexistent_tool not found" 

def test_extract_single_artifact():
    conv = Conversation()
    conv.messages = [{
        "role": "user",
        "content": '''
            <artifact identifier="123abc" type="text/plain" title="Test Note">
            Hello world
            </artifact>
        '''
    }]
    
    artifacts = conv._extract_artifacts()
    assert len(artifacts) == 1
    assert artifacts[0].identifier == "123abc"
    assert artifacts[0].type == "text/plain"
    assert artifacts[0].title == "Test Note"
    assert artifacts[0].content == "Hello world"

def test_extract_multiple_artifacts():
    conv = Conversation()
    conv.messages = [{
        "role": "user",
        "content": '''
            <artifact identifier="123" type="text/plain" title="First">One</artifact>
            <artifact identifier="456" type="text/markdown" title="Second">Two</artifact>
        '''
    }]
    
    artifacts = conv._extract_artifacts()
    assert len(artifacts) == 2
    assert {a.identifier for a in artifacts} == {"123", "456"}

def test_duplicate_identifiers_keeps_latest():
    conv = Conversation()
    conv.messages = [
        {
            "role": "user",
            "content": '<artifact identifier="123" type="text/plain" title="Old">Old content</artifact>'
        },
        {
            "role": "assistant",
            "content": '<artifact identifier="123" type="text/plain" title="New">New content</artifact>'
        }
    ]
    
    artifacts = conv._extract_artifacts()
    assert len(artifacts) == 1
    assert artifacts[0].content == "New content"
    assert artifacts[0].title == "New"

def test_no_artifacts():
    conv = Conversation()
    conv.messages = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there"}
    ]
    
    artifacts = conv._extract_artifacts()
    assert len(artifacts) == 0

def test_artifacts_in_tool_results():
    conv = Conversation()
    conv.messages = [{
        "role": "user",
        "content": [
            {
                "type": "tool_result",
                "content": '<artifact identifier="tool123" type="text/plain" title="Tool Result">Tool output</artifact>'
            }
        ]
    }]
    
    artifacts = conv._extract_artifacts()
    assert len(artifacts) == 1
    assert artifacts[0].identifier == "tool123"