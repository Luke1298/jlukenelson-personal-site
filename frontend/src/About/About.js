import './About.css';
import linkedinShot from './media/personal_pic.jpeg';

function About() {
  return (
      <div className="about-page">
        <h1 className="about-page-title">
          J. Luke Nelson
        </h1>
        <div className="about-page-content">
          <div className="left">
              <img alt="J. Luke Nelson's portrait" src={linkedinShot} className="linkedin-shot"/>
            <div className="left-links">
              <a href="https://www.linkedin.com/in/j-luke-nelson-500b8483">LinkedIn</a>
              <a href="https://github.com/Luke1298">Github</a>
              <a href="https://twitter.com/isomorphic2baz">Twitter</a>
            </div>
          </div>
          <div className="right">
            <h2 className="about-page-bio-short-title">Synopsis</h2>
              <p> J. Luke Nelson is an accomplished problem solver with an undergraduate degree in applied and computational mathematics, and a proven track record in data engineering, software development, and cutting-edge technologies. As a passionate coder, he has contributed significantly to various projects, consistently demonstrating his commitment to leveraging data-driven insights for informed decision-making and meaningful impact.</p>
              <p> Currently pursuing a Master's degree in Computer Science, Luke is set to graduate in the summer of 2023, expanding his knowledge and expertise in the field. As a certified AWS Solutions Architect, he has hands-on experience in designing and implementing real-time analytics pipelines, cost-effective low-scale solutions, and scalable architectures to meet evolving business needs using top industry tools and technologies.</p>
              <p> Notable achievements in Luke's career include the development of innovative solutions across all aspects of the software development process, and his active contributions to open-source projects. Currently thriving at Videra Health, he enjoys the challenges and rewarding experiences that come with his role. J. Luke Nelson's unique blend of academic and professional experience, combined with his expertise in high-demand skills, makes him an excellent fit for organizations seeking to unlock the full potential of their data-driven initiatives and stay ahead in the competitive tech landscape. While he is dedicated to his current position, Luke remains open to exploring exceptional opportunities for growth and impact.</p>
            <h2 className="about-page-bio-short-title">Reach Out</h2>
             <p> Email me anytime at: <a className="color-link" href="mailto:lukenelson1298@gmail.com">lukenelson1298@gmail.com</a></p>
          </div>
        </div>
      </div>
  );
}

export default About;
