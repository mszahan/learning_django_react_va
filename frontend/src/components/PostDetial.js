import React, { useState, useEffect} from 'react';
import axiosInstance from '../axios';
import { useParams } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';





export default function PostDetial() {
    const { slug } = useParams();

	const [data, setData] = useState({ posts: [] });

	useEffect(() => {
		axiosInstance.get(slug).then((res) => {
			setData({ posts: res.data });
			console.log(res.data);
		});
	}, [setData]);

    return (
        <Container>
            <Row>
                <Col md={10}>
                    <h1>
                        {data.posts.title}
                    </h1>
                    <p>
                        {data.posts.content}
                    </p>
                </Col>
            </Row>
        </Container>
    );




}



