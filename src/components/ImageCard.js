import React from 'react';

function ImageCard({ image, logo, profileImg }) {
  return (
    <div className="image-card">
      <img src={image.src} alt={image.alt} />
      <div className="hover-info">
        <img src={logo} alt="Gokei Logo" className="logo" />
        <div className="bottom-info">
          <img src={profileImg} alt="Author" className="author-img" />
          <span className="author-text">{image.author}</span>
        </div>
      </div>
      <div className="tags">
        {image.tags.map((tag, index) => (
          <span key={index} className="tag">{tag}</span>
        ))}
      </div>
    </div>
  );
}

export default ImageCard;