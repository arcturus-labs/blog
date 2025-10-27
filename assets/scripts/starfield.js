class Star {
    constructor(canvas, x, y, radius) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.mass = Math.PI * radius * radius; // Mass proportional to area
        this.velocity = {
            x: (Math.random() - 0.5) * 0.1, // Small initial random velocity
            y: (Math.random() - 0.5) * 0.1
        };
        this.active = true; // Flag to track if star should be removed
    }

    draw() {
        this.ctx.beginPath();
        const inner_radius_fraction = 1.0/4;
        this.ctx.moveTo(this.x, this.y - this.radius); // North point
        this.ctx.lineTo(this.x + this.radius*inner_radius_fraction, this.y - this.radius*inner_radius_fraction);
        this.ctx.lineTo(this.x + this.radius, this.y); // East point
        this.ctx.lineTo(this.x + this.radius*inner_radius_fraction, this.y + this.radius*inner_radius_fraction);
        this.ctx.lineTo(this.x, this.y + this.radius); // South point
        this.ctx.lineTo(this.x - this.radius*inner_radius_fraction, this.y + this.radius*inner_radius_fraction);
        this.ctx.lineTo(this.x - this.radius, this.y); // West point
        this.ctx.lineTo(this.x - this.radius*inner_radius_fraction, this.y - this.radius*inner_radius_fraction);
        this.ctx.closePath();
        this.ctx.fillStyle = 'rgba(255,255,255,0.8)';
        this.ctx.fill();
    }

    update(stars, mouse) {
        // Cursor repulsion
        if (mouse.x && mouse.y) {
            const dx = mouse.x - this.x;
            const dy = mouse.y - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy) + 50; // 20 added so that the cursor can't knock stars out of the screen
            
            // Strong repulsion force within 100 pixels of cursor
            if (distance < 100) {
                const repulsionStrength = 50;  // Adjust for stronger/weaker effect
                const force = repulsionStrength / (distance * distance);
                this.velocity.x += (force * dx / distance);
                this.velocity.y += (force * dy / distance);
            }
        }

        // Calculate gravitational forces from all other stars
        stars.forEach(star => {
            if (star === this || !star.active) return;

            const dx = star.x - this.x;
            const dy = star.y - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            // Check for collision/merging
            if (distance < 3) {
                if (this.mass <= star.mass) {
                    this.active = false; // Mark for removal
                    return;
                }
            }

            // Gravitational force = G * (m1 * m2) / r^2
            const G = 0.005; // Gravitational constant (adjust for desired strength)
            const force = G * (this.mass * star.mass) / (distance * distance);

            // Convert force to acceleration components (F = ma, so a = F/m)
            const ax = (force * dx / distance) / this.mass;
            const ay = (force * dy / distance) / this.mass;

            // Update velocity
            this.velocity.x += ax;
            this.velocity.y += ay;
        });

        // Apply velocity with damping
        this.x += this.velocity.x;
        this.y += this.velocity.y;
        this.velocity.x *= 0.99; // Slight damping to prevent chaos
        this.velocity.y *= 0.99;

        // Wrap around screen edges
        if (this.x < 0) this.x = this.canvas.width;
        if (this.x > this.canvas.width) this.x = 0;
        if (this.y < 0) this.y = this.canvas.height;
        if (this.y > this.canvas.height) this.y = 0;
    }
}

function createNewStar(canvas, radius) {
    return new Star(
        canvas,
        Math.random() * canvas.width,
        Math.random() * canvas.height,
        radius
    );
}

function initStarField() {
    const canvas = document.getElementById('starfield');
    const ctx = canvas.getContext('2d');

    // Set canvas size
    function resize() {
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = canvas.parentElement.clientHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    // Track mouse position
    const mouse = { x: undefined, y: undefined };
    canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouse.x = e.clientX - rect.left;
        mouse.y = e.clientY - rect.top;
    });
    canvas.addEventListener('mouseleave', () => {
        mouse.x = undefined;
        mouse.y = undefined;
    });

    // Create initial stars
    let stars = [];
    const starCount = Math.floor((canvas.width * canvas.height) / 8000);
    for (let i = 0; i < starCount; i++) {
        stars.push(createNewStar(canvas, Math.random() * 5 + 2));
    }

    // Animation loop
    function animate() {
        ctx.fillStyle = 'rgb(0, 78, 128)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Update and draw active stars
        stars.forEach(star => {
            if (star.active) {
                star.update(stars, mouse);
                star.draw();
            }
        });

        // Replace inactive stars
        stars = stars.map(star => {
            if (!star.active) {
                return createNewStar(canvas, star.radius);
            }
            return star;
        });

        
        requestAnimationFrame(animate)
    }
    animate();
}

// Initialize when the DOM is loaded
document.addEventListener('DOMContentLoaded', initStarField);