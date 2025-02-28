import React, { useEffect, useState} from 'react';
import { api } from '../services/api';

const Home = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        // URL del endpoint en Django
        api.get('/productos/').then(response => setProducts(response.data.results)).catch(error => console.error("Error al obtener productos: ", error));

    }, []);

    return (
        <div>
            <h1>Bienvenido a CrodiShop</h1>
            <ul>
                {products.map(product => (
                    <li key={product.id}>{product.nombre} - ${product.precio}</li>
                ))}
            </ul>
        </div>
    );
};
export default Home;