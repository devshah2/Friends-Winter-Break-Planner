import Button from 'react-bootstrap/Button';
import './App.css'
import Form from "react-bootstrap/Form";

export default function App() {
    return (
        <div class="box">
        <h1>hi</h1>
        <Form>
        <Form.Label>Add a new resident</Form.Label>
        <Form.Group className="mb-3" controlId="first_name">
                    <Form.Label>First Name</Form.Label>
                    <Form.Control name="first_name" required/>
                </Form.Group>
          <Button variant="primary" type="submit">
                      Submit
                  </Button>
        </Form>
        </div>
        
    )
}