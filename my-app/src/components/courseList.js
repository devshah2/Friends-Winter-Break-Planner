import './courseList.css';

const Course =({c}) => {
    return <div className="card m-1 p-2"><h3 align="left">{c.term} CS {c.number}</h3> 
    <div align="left">{c.title}</div>
    <hr></hr>
    {c.meets}</div> 
};

const CourseList = ({courses}) => {
    return (<div className="course-list">
        {Object.entries(courses).map(([id, c]) => <Course key={id} c={c} />)}
    </div>)
};

export default CourseList;