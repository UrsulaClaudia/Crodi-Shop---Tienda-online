import React, { useEffect, useState } from "react";
import { api } from "../services/api";
import { Card, Button } from 'react-bootstrap';

const Catalogo = () => {
    const [productos, setProductos] = useState([]);

    useEffect(() => {
        api.get('/productos%').then(response => setProductos(response.data.results)).catch(error=>console.error("Error al obtener productos: ", error));
    }, []);

    return (
        <div className="containes mt-4">
            <h2>Catalogo de Productos</h2>
            <div className="row">
                {productos.map(producto => (
                    <div key={producto.id} className="col-md-4">
                        <Card className="mb-3">
                            <Card.Img variant="top" src={producto.imagen} alt={producto.nombre} />
                            <Card.Body>
                                <Card.Title>{producto.nombre}</Card.Title>
                                <Card.Text>Precio: ${producto.precio}</Card.Text>
                                <Button variant="primary">Agregar al carrito</Button>
                            </Card.Body>
                        </Card>

                    </div>
                ))}

            </div>
        </div>
    );
};

export default Catalogo;