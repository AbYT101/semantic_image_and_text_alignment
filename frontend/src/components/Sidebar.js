import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Sidebar = () => {
  const location = useLocation();

  return (
    <div className="w-64 h-screen bg-gray-800 text-white">
      <h2 className="text-2xl p-4"></h2>
      <nav>
        <ul>
          <li className={`p-4 ${location.pathname === '/' ? 'bg-gray-900' : ''}`}>
            <Link to="/" className="block hover:bg-gray-900 px-2 py-1 rounded">
              Compose Image
            </Link>
          </li>
          <li className={`p-4 ${location.pathname === '/evaluate' ? 'bg-gray-900' : ''}`}>
            <Link to="/evaluate" className="block hover:bg-gray-900 px-2 py-1 rounded">
              Evaluate Image
            </Link>
          </li>
          <li className={`p-4 ${location.pathname === '/storyboard' ? 'bg-gray-900' : ''}`}>
            <Link to="/storyboard" className="block hover:bg-gray-900 px-2 py-1 rounded">
              Build Storyboard
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;
