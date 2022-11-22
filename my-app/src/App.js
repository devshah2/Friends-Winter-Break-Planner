import './App.css';
import Banner from './components/banner';
import CourseList from './components/courseList';
import 'bootstrap/dist/css/bootstrap.min.css';
import schedule from './utilities/data'

export default App;


function App() {
  return (
    <div className="App">
      <CourseList courses={schedule().courses} />
    </div>
  );
}

// export default App;
