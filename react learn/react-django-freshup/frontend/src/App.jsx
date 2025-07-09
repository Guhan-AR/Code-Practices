// src/App.jsx
import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // We will add some basic styling

// Define the API URL
const API_URL = 'http://127.0.0.1:8000/api/posts/';

function App() {
  // State variables
  const [posts, setPosts] = useState([]);
  const [isEditing, setIsEditing] = useState(false);
  const [currentPost, setCurrentPost] = useState({ id: null, title: '', content: '' });
  const [imageFile, setImageFile] = useState(null);

  // Fetch all posts from the API when the component mounts
  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = async () => {
    try {
      const response = await axios.get(API_URL);
      setPosts(response.data);
    } catch (error) {
      console.error("There was an error fetching the posts:", error);
    }
  };

  // Handle changes in form inputs
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCurrentPost({ ...currentPost, [name]: value });
  };

  // Handle file selection
  const handleFileChange = (e) => {
    setImageFile(e.target.files[0]);
  };

  // Handle form submission (for both create and update)
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Use FormData to send file and text data together
    const formData = new FormData();
    formData.append('title', currentPost.title);
    formData.append('content', currentPost.content);
    if (imageFile) {
      formData.append('image', imageFile);
    }

    try {
      if (isEditing) {
        // Update existing post
        // Note: For PUT, some backends might require the image. Re-upload or adjust backend logic.
        await axios.put(`${API_URL}${currentPost.id}/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
      } else {
        // Create new post
        await axios.post(API_URL, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
      }
      // Reset form and refresh post list
      resetForm();
      fetchPosts();
    } catch (error) {
      console.error("There was an error submitting the form:", error);
    }
  };

  // Set the form to edit mode and populate it with post data
  const handleEdit = (post) => {
    setIsEditing(true);
    setCurrentPost({ id: post.id, title: post.title, content: post.content });
    setImageFile(null); // Clear previous file selection
  };

  // Delete a post
  const handleDelete = async (id) => {
    try {
      await axios.delete(`${API_URL}${id}/`);
      fetchPosts(); // Refresh the list
    } catch (error) {
      console.error("There was an error deleting the post:", error);
    }
  };

  // Reset the form state
  const resetForm = () => {
    setIsEditing(false);
    setCurrentPost({ id: null, title: '', content: '' });
    setImageFile(null);
  };

  return (
    <div className="app-container">
      <h1>Post It!</h1>

      {/* Form for Creating and Editing Posts */}
      <form onSubmit={handleSubmit} className="post-form">
        <h2>{isEditing ? 'Edit Post' : 'Create a New Post'}</h2>
        <input
          type="text"
          name="title"
          value={currentPost.title}
          onChange={handleInputChange}
          placeholder="Title"
          required
        />
        <textarea
          name="content"
          value={currentPost.content}
          onChange={handleInputChange}
          placeholder="Content"
          required
        />
        <input type="file" onChange={handleFileChange} />
        <div className="form-buttons">
          <button type="submit">{isEditing ? 'Update' : 'Create'}</button>
          {isEditing && <button type="button" onClick={resetForm}>Cancel</button>}
        </div>
      </form>

      {/* List of Posts */}
      <div className="posts-list">
        <h2>All Posts</h2>
        {posts.map((post) => (
          <div key={post.id} className="post-item">
            <h3>{post.title}</h3>
            <p>{post.content}</p>
            {post.image && (
              <img
                src={post.image} // Django REST Framework provides the full URL
                alt={post.title}
                className="post-image"
              />
            )}
            <div className="post-actions">
              <button onClick={() => handleEdit(post)}>Edit</button>
              <button onClick={() => handleDelete(post.id)}>Delete</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
