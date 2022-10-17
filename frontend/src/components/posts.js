import React from "react";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { Link } from 'react-router-dom';



const Posts = (props) =>{
    const { posts } = props;
    if (!posts || posts.length === 0) return <p>No posts added yet</p>;
    return(
        <React.Fragment>
            <Container>
                <Row>
                    {posts.map((post) => {
                        return(
                            <Col key={post.id} xs={12} md={4}>
                                    <Card>
                                        <Card.Img variant="top" src="https://source.unsplash.com/random" style={{ maxHeight: 200,}} />
                                        <Card.Body>
                                            <Card.Title> <strong> {post.title} </strong> </Card.Title>
                                            <Card.Text>
                                            {post.excerpt.substr(0, 60)}....
                                            </Card.Text>
                                            <Link to={'post/' + post.slug}>
                                            <Button variant="primary">View post</Button>
                                            </Link>
                                        </Card.Body>
                                    </Card>
                            </Col>
                        );
                    })}
                </Row>
            </Container>
        </React.Fragment>
    );
};

export default Posts;