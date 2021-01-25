import './About.css';
import linkedinShot from './media/personal_pic.jpeg';

function About() {
  return (
      <div className="about-page">
        <div className="about-page-title">
          J. Luke Nelson
        </div>
        <div className="about-page-content">
          <div className="left">
              <img src={linkedinShot} className="linkedin-shot"/>
            <div className="left-links">
              <a href="https://www.linkedin.com/in/j-luke-nelson-500b8483">LinkedIn</a>
              <a href="https://github.com/Luke1298">Github</a>
              <a href="https://twitter.com/isomorphic2baz">Twitter</a>
            </div>
          </div>
          <div className="right">
            <div className="about-page-bio-short-title">Synopsis</div>
            <p> J. Luke Nelson is a problem solver with professional experience in Data Engineering and Software Engineering. He is a passionate futurist who constantly considers how data can help humanity make informed decisions.</p>
            <div className="about-page-bio-short-title">Details</div>
            <p> I grew up in Las Vegas Nevada, as the youngest of 8 children. My father was a software engineer for most of his career, as such he and I frequently discussed topics in computer science, such as adding numbers in binary or searching a graph. When I was 14 I began writing code. In exchange for babysitting my oldest brother's (who was also a software engineer) kids he would help tutor me in coding and software engineering principles. He helped to teach me about reusable design and how to effectively organize projects. When I started my Undergraduate Degree at Brigham Young University I was 16 years old, and was fortunate to get an internship at a local company during my first semester at BYU. </p>

             <p> My wife and I were married in the summer of 2020. When I'm not coding you'll find me cooking with her. We try a new recipe a couple times every week.</p>
             <div className="about-page-bio-short-title">Reach Out</div>
             <p> Email me anytime at: <a className="color-link" href="mailto:lukenelson1298@gmail.com">lukenelson1298@gmail.com</a></p>
          </div>
        </div>
      </div>
  );
}

export default About;
