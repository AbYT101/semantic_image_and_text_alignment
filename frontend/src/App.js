  import React from 'react';
  import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
  import ComposeImage from './components/ComposeImage';
  import EvaluateImage from './components/EvaluateImage';
  import BuildStoryboard from './components/BuildStoryboard';
  import Sidebar from './components/Sidebar';
  import { Toaster } from 'react-hot-toast';

  const App = () => {
    return (
      <Router>
        <div className="flex flex-col h-screen">
          {/* Top Navigation */}
          <nav className="bg-gray-800 text-white p-4 fixed w-full z-10">
            <div className="mx-auto flex justify-between items-center">
              {/* Logo on the left */}
              <Link to="/" className="flex items-center">
                <img src="https://sso.adludio.com/static/media/adludio_logo_white.0bde82cd.png" alt="Logo" className="h-8 mr-2" /> {/* Adjust logo size as needed */}
                <span className="text-2xl font-bold hover:text-green-400"></span> {/* Adjust text size and styling */}
              </Link>

              {/* Text on the right */}
              <div className="space-x-4">
                <Link to="/storyboard" className="hover:text-green-400">
                  {/* Build Storyboard */}
                </Link>
              </div>
            </div>
          </nav>

          {/* Main Content Area with Sidebar */}
          <div className="flex flex-1 mt-10"> {/* Adjust margin-top to accommodate fixed nav height */}
            <Sidebar />
            <div className="flex-1 p-4 pt-30">
              <Routes>
                <Route path="/" element={<ComposeImage />} />
                <Route path="/evaluate" element={<EvaluateImage />} />
                <Route path="/storyboard" element={<BuildStoryboard />} />
              </Routes>
            </div>
          </div>

          {/* Toaster for Notifications */}
          <Toaster position="top-center" />
        </div>
      </Router>
    );
  };

  export default App;
