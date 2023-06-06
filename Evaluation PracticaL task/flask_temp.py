from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    # Load the Three.js library from a CDN
    three_js_script = '''
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/110/three.min.js"></script>
    '''

    # Define the HTML template with Three.js code to render the pyramid
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pyramid Example</title>
        {{ three_js_script }}
        <style>
            body { margin: 0; }
            canvas { display: block; }
        </style>
    </head>
    <body>
        <script>
            // Set up the scene, camera, and renderer
            var scene = new THREE.Scene();
            var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            var renderer = new THREE.WebGLRenderer();
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);

            // Create the pyramid geometry
            var geometry = new THREE.Geometry();
            geometry.vertices.push(
                new THREE.Vector3(1, 1, 0),
                new THREE.Vector3(-1, 1, 0),
                new THREE.Vector3(-1, -1, 0),
                new THREE.Vector3(1, -1, 0),
                new THREE.Vector3(0, 0, {{ pyramid_height }})
            );
            geometry.faces.push(
                new THREE.Face3(0, 1, 4),
                new THREE.Face3(1, 2, 4),
                new THREE.Face3(2, 3, 4),
                new THREE.Face3(3, 0, 4)
            );

            // Create the pyramid material and mesh
            var material = new THREE.MeshBasicMaterial({ color: 0x00ff00, wireframe: true });
            var pyramid = new THREE.Mesh(geometry, material);
            scene.add(pyramid);

            // Set up the camera position
            camera.position.z = 5;

            // Render the scene
            function animate() {
                requestAnimationFrame(animate);
                pyramid.rotation.x += 0.01;
                pyramid.rotation.y += 0.01;
                renderer.render(scene, camera);
            }
            animate();
        </script>
    </body>
    </html>
    '''

    # Render the template with the pyramid height value
    rendered_template = render_template_string(template, pyramid_height=2.5, three_js_script=three_js_script)
    return rendered_template


if __name__ == '__main__':
    app.run(debug=True)