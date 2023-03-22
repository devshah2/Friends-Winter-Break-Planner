import Button from 'react-bootstrap/Button';
import './homepage.css'
import Form from "react-bootstrap/Form";
import Select from 'react-select';
export default function homepage() {
    return (
        <div>
        <div className="box">
            <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="first_name">
                    <Form.Label>Search for a resident</Form.Label>
                    <Select className="serachbar"
                        name="searchbar"
                        placeholder="Select resident..."
                        options={names}
                        required
                    />
               </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form> 
        </div>
        <div className="box">
            <Form onSubmit={handleSubmitNew}>
                <Form.Label>Add a new resident</Form.Label>
                <Form.Group className="mb-3" controlId="first_name">
                    <Form.Label>First Name</Form.Label>
                    <Form.Control name="first_name" required/>
                </Form.Group>
                <Form.Group className="mb-3" controlId="last_name">
                    <Form.Label>Last Name</Form.Label>
                    <Form.Control name="last_name" required/>
                </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
        </div>
        </div>
        
    )
}