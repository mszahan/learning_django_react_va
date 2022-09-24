import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { Container } from 'react-bootstrap';
import { NavLink } from 'react-router-dom';



function Header() {
    const handleSelect = (eventKey) => alert(`selected ${eventKey}`);

  return (
    <Container className='m-1'>
    <Nav activeKey="1" onSelect={handleSelect}>
      <Nav.Item>
        <Nav.Link eventKey="1">
          
        <NavLink 
        to='/'>
          Home
        </NavLink>
        </Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="2" title="Item">
          Posts
        </Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="3" >
          About
        </Nav.Link>
      </Nav.Item>
      <NavDropdown title="Profile" id="nav-dropdown">
        <NavDropdown.Item eventKey="4.1">
          <NavLink
          to='register/'
          >
          Register
          </NavLink>
          </NavDropdown.Item>
        <NavDropdown.Item eventKey="4.2">
        <NavLink
          to='login/'
          >
          Login
          </NavLink>
          </NavDropdown.Item>
        <NavDropdown.Item eventKey="4.3">Something else here</NavDropdown.Item>
        <NavDropdown.Divider />
        <NavDropdown.Item eventKey="4.4">Separated link</NavDropdown.Item>
      </NavDropdown>
    </Nav>
    </Container>
  );
}

export default Header;