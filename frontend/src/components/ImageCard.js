import React from 'react';

const ImageCard = ({ image }) => {
  return (
    <div className="image-card">
      <img src={image.url} alt={image.id} />
      <div className="hover-info">
        <img src={`${process.env.PUBLIC_URL}/logo.png`} alt="Gokei Logo" className="logo" />
        <div className="bottom-info">
          <img src={image.author.profile_image} alt="Author" className="author-img" />
          <span className="author-text">
            {image.author.name}: {image.author.username}
            {image.author.twitter_username && (
              <span> (X: @{image.author.twitter_username})</span>
            )}
          </span>
        </div>
      </div>
      <div className="tags">
        {image.tags.map((tag, index) => (
          <span key={index} className="tag">{tag.title}</span>
        ))}
      </div>
    </div>
  );
}

export default ImageCard;