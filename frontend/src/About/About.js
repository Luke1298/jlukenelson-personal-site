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
              <p> J. Luke Nelson is an accomplished problem solver with an undergraduate degree in applied and computational mathematics, and a proven track record in data engineering, software development, and cutting-edge technologies. As a passionate coder, he has contributed significantly to various projects, consistently demonstrating his commitment to leveraging data-driven insights for informed decision-making and meaningful impact.</p>
              <p> Currently pursuing a Master's degree in Computer Science, Luke is set to graduate in the summer of 2023, expanding his knowledge and expertise in the field. As a certified AWS Solutions Architect, he has hands-on experience in designing and implementing real-time analytics pipelines, cost-effective low-scale solutions, and scalable architectures to meet evolving business needs using top industry tools and technologies.</p>
              <p> Notable achievements in Luke's career include the development of innovative solutions acorss all aspects of the software development process, and his active contributions to open-source projects. His unique blend of academic and professional experience, combined with his expertise in high-demand skills, make J. Luke Nelson an ideal candidate for organizations looking to unlock the full potential of their data-driven initiatives and stay ahead in the competitive tech landscape.</p>
            <div className="about-page-bio-short-title">Reach Out</div>
             <p> Email me anytime at: <a className="color-link" href="mailto:lukenelson1298@gmail.com">lukenelson1298@gmail.com</a></p>
          </div>
        </div>
      </div>
  );
}

export default About;
