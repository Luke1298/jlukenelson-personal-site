import React, { useState, useEffect } from "react";
import Confetti from "react-confetti";
import "./BirthdayMessage.css";

function BirthdayMessage() {
  const [showConfetti, setShowConfetti] = useState(true);

  // Stop confetti after a few seconds
  useEffect(() => {
    const timer = setTimeout(() => setShowConfetti(false), 5000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="birthday-message-outer">
      <Confetti recycle={showConfetti}/>
      <div className="birthday-message fade-in">
        <h1>🎉 Happy 18th Birthday, Lily! 🎉</h1>
        <p>Welcome to adulthood! May this year be filled with excitement, joy, and wonderful surprises! 🎈🎂</p>
        <p>
          I’m so grateful that my kids have you as their aunt. You’re an
          incredible example to them of dilegence, basketball skill, and determination. I know
          they look up to you in many ways. Thank you for being there for them and
          being willing to play with Eden and to hold baby Conley. Here’s to all
          the amazing adventures awaiting you this year and beyond.
        </p>
        <p>&mdash; J Luke Nelson</p>
      </div>
    </div>
  );
}

export default BirthdayMessage;

