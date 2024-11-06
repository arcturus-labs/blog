
import anthropic
import json

class Artifact:
    def __init__(self, identifier, type, title, content):
        self.identifier = identifier
        self.type = type
        self.title = title
        self.content = content

    def __str__(self):
        return f"<artifact identifier={self.identifier} type={self.type} title={self.title}>\n{self.content}\n</artifact>"
    
class Tool:
    def __init__(self, schema, callable):
        self.schema = schema
        self.callable = callable
        self.name = schema["name"]

class Conversation:
    def __init__(self, tools=None,filename=None):
        self.client = anthropic.Anthropic()
        self.model = "claude-3-sonnet-20240229"
        self.messages = []
        self.tools = tools or []
        self.filename = None
        if filename:
            self.filename = filename
            try:
                with open(filename, "r") as file:
                    self.messages = json.load(file)
            except FileNotFoundError:
                print(f"File {filename} not found")
        
    def say(self, message):
        self.messages.append(
            {
                "role": "user", 
                "content": message
            }
        )
        system_message = self._generate_system_message()
        tools = [t.schema for t in self.tools]
        response = self.client.messages.create(
            model=self.model,
            system=system_message,
            messages=self.messages,
            max_tokens=3000,
            temperature=0.7,
            tools=tools,
        )

        # Handle potential tool use
        assistant_messages = []
        while response.stop_reason == "tool_use":
            print("\n"+str(response.content))

            tool_result_messages  = []
            for block in response.content:
                if block.type != "tool_use":
                    # TODO: this could be improved. As is we're going to just concatenate the text of all the blocks.
                    # This might not make sense to the reader since the tool calls are missing and the assistant might refer to them.
                    # An improvement would be to have the assistant say something like "I used the following tools to answer the question: ..."
                    # and then list the tools used and their results.
                    assistant_messages.append(block.text)
                else:
                    tool_use = block
                    tool_name = tool_use.name
                    tool_input = tool_use.input
                    tool_result = self._process_tool_call(tool_name, tool_input)
                    tool_result_messages.append({
                        "type": "tool_result",
                        "tool_use_id": tool_use.id,
                        "content": tool_result,
                    })
            
            self.messages.append({"role": "assistant", "content": response.content})
            self.messages.append({
                "role": "user",
                "content": tool_result_messages,
            })
            
            # Get final response after tool use
            response = self.client.messages.create(
                model=self.model,
                system=system_message,
                messages=self.messages,
                max_tokens=3000,
                temperature=0.7,
                tools=tools,
            )
        
        assistant_messages.append(response.content[0].text)
        assistant_message = "\n".join(assistant_messages)
        self.messages.append({"role": "assistant", "content": assistant_message})
        if self.filename:
            self._save()
        print(assistant_message)
        return assistant_message
    
    def _process_tool_call(self, tool_name, tool_input):
        for tool in self.tools:
            if tool.name == tool_name:
                return tool.callable(tool_input)
        raise Exception(f"Tool {tool_name} not found")
    
    def _generate_system_message(self):
        artifacts = self._extract_artifacts()
        artifacts_info = "\n".join([str(artifact) for artifact in artifacts])
        system_message = f"""\
You are a helpful assistant.

<artifacts_info>
Artifacts are self-contained pieces of content that can be referenced in the conversation. The assistant can generate artifacts during the course of the conversation upon request of the user. Artifacts have the following format:

```
<artifact identifier="hexidecimal-hash" type="mime_type" title="title">
...actual content of the artifact...
</artifact>
```

example identifiers: 18bacG4a, 3baf9f83, 98acb34d
example types: text/markdown, text/plain, application/json, image/svg+xml
example titles: "Simple Python factorial script", "Blue circle SVG", "Metrics dashboard React component"

<artifact_instructions>
- The user has access to the artifacts, therefore the assistant should not reproduct the full content of the artifact in the conversation, but should instead reference it by its `identifier` using an anchor tag like this: `<a href="#18bacG4a">linked text</a>`.
- The linked text should make sense in the context of the conversation. The assistant must supply the linked text.
- The user can similarly refer to the artifacts via an anchor. But they can also just say "the thing we were discussing earlier".
- Artifact titles must be short, descriptive, and unique.
- All existing artifacts are presented in the <artifacts> tag below.
</artifact_instructions>

</artifacts_info>

<artifacts>
{artifacts_info}
</artifacts>
"""
        return system_message
    
    def _extract_artifacts(self):
        return []
    def _save(self):
        if self.filename:
            with open(self.filename, "w") as file:
                messages_to_save = []
                for message in self.messages:
                    if isinstance(message['content'], list):
                        # Handle list of content blocks
                        new_content = []
                        for block in message['content']:
                            if hasattr(block, 'dict'):
                                new_content.append(block.dict())
                            else:
                                new_content.append(block)
                        messages_to_save.append({
                            'role': message['role'],
                            'content': new_content
                        })
                    else:
                        # Content is a simple string or already a dict
                        messages_to_save.append(message)
                json.dump(messages_to_save, file)



