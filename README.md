# Golden Gate Image Gallery

## Overview

This project showcases images of the Golden Gate fetched from the Unsplash API. The application displays these images in a grid and provides hover effects to show additional information about the author, such as profile picture, username, and Twitter handle, along with corresponding tags for each image.

---

### Tecnologías Utilizadas en el Proyecto

1. **Python**
   - **Razón**: Es un lenguaje de programación versátil y potente utilizado para el backend de la aplicación. Se elige por su legibilidad, simplicidad y el vasto ecosistema de bibliotecas y frameworks que aceleran el desarrollo. Ademas es el lenguaje que mas experiencia tengo

2. **Flask**
   - **Razón**: Por que es un framework web ligero para Python que proporciona las herramientas esenciales para construir aplicaciones web de manera rápida y con un mínimo de complejidad.

3. **SQLAlchemy**
   - **Razón**: Es una potente herramienta SQL y una biblioteca de mapeo objeto-relacional (ORM) para Python.

4. **React.js**
   - **Razón**: Se elige por su arquitectura basada en componentes, lo que facilita la construcción y el mantenimiento de interfaces de usuario complejas.

5. **Docker**
   - **Razón**: Se elige por su capacidad para proporcionar entornos consistentes en diferentes etapas del desarrollo, desde el desarrollo local hasta la producción.

6. **Docker Compose**
   - **Razón**: Se elige por su capacidad para gestionar múltiples servicios de contenedores (como el backend y el frontend) con un solo comando, simplificando los flujos de trabajo de desarrollo y despliegue.

7. **Axios**
    - **Razón**: Axios es un cliente HTTP basado en promesas para JavaScript. Se elige para realizar solicitudes HTTP desde el navegador, facilitando la comunicación entre el frontend y el backend de la aplicación.

8. **Masonry**
    - **Razón**: Masonry es una biblioteca de diseño de cuadrícula en JavaScript. Se elige para crear diseños receptivos y dinámicos que se ajusten a diferentes tamaños de pantalla y cantidades de contenido, mejorando la presentación visual del grid de imágenes.

Al aprovechar estas tecnologías, el proyecto asegura una aplicación robusta, escalable y mantenible que puede ser desarrollada, probada y desplegada de manera eficiente. Cada tecnología se elige en función de sus fortalezas y de cómo encaja en la arquitectura y los requisitos generales del proyecto.

---

## Features

- Fetch images from Unsplash based on the search term "Golden Gate".
- Display the first 30 images in a responsive grid.
- Implement hover effects to show the author's profile picture, username, and Twitter handle.
- Include corresponding tags for each image.

## Technologies

- Flask for the backend.
- React.js for the frontend.
- Unsplash API for fetching images.
- HTML/CSS/JavaScript for displaying images and hover effects.
- Docker for containerization.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Unsplash API Access Key (Sign up at [Unsplash Developers](https://unsplash.com/developers))

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/golden-gate-image-gallery.git
    cd golden-gate-image-gallery
    ```

2. Set up environment variables:
    - Create a `.env` file in the root directory and add your Unsplash API key:
    ```env
    UNSPLASH_API_KEY=your_unsplash_api_key
    ```

### Running the Application

1. **Build and start the Docker containers**:
    ```bash
    docker-compose up --build
    ```

2. **Access the Frontend**:
    - Navigate to `http://localhost:3000` in your web browser.

3. **Access the Backend**:
    - The Flask API will be running at `http://localhost:5000`.

### Running Python Tests with Docker

```bash
docker run -it --rm -v $(PWD):/app -p 5000:5000 golden-gate-web-backend pytest
```


## Project Structure

Here is an overview of the project structure:

```
.
├── README.md
├── backend
│   ├── Dockerfile
│   ├── app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── routes.py
│   ├── images_data
│   ├── requirements.txt
│   └── run.py
├── docker-compose.yml
└── frontend
    ├── Dockerfile
    ├── package-lock.json
    ├── package.json
    ├── public
    │   ├── favicon.ico
    │   ├── index.html
    │   ├── logo.png
    │   ├── manifest.json
    │   └── robots.txt
    ├── src
    │   ├── App.css
    │   ├── App.js
    │   ├── App.test.js
    │   ├── assets
    │   │   └── images
    │   │       ├── placeholders
    │   │       │   ├── image1.jpg
    │   │       │   ├── image2.jpg
    │   │       │   ├── image3.jpg
    │   │       │   ├── image4.jpg
    │   │       │   ├── image5.jpg
    │   │       │   ├── image6.jpg
    │   │       │   └── logo.png
    │   │       └── users
    │   │           └── profile-1.avif
    │   ├── components
    │   │   ├── ImageCard.js
    │   │   └── ImageGrid.js
    │   ├── index.css
    │   ├── index.js
    │   ├── reportWebVitals.js
    │   ├── setupTests.js
    │   └── styles
    │       ├── grid.css
    │       └── main.css
    └── tests
        ├── Grid.test.js
        └── ImageCard.test.js
```

### Directory and File Description


- **docker-compose.yml**: Docker Compose configuration file to set up the backend and frontend services.


- **backend/**: Contains the backend code using Flask.
  - **app/**: Contains the Flask application code.
  - **images_data/**: Directory to store the SQLite database file.
  - **requirements.txt**: Python dependencies for the backend.
  - **run.py**: Entry point to run the Flask application.
  

- **frontend/**: Contains the frontend code using React.js.
  - **public/**: Contains the static files for the React app.
  - **src/**: Contains the source code for the React app.
    - **assets/**: Contains static assets like images.
      - **images/**: Contains image files used in the app.
    - **components/**: Contains React components.
    - **styles/**: Contains additional CSS files.
  - **tests/**: Contains test files for the React components.

## Contribution

Feel free to fork this repository and make contributions. Pull requests are welcome.
