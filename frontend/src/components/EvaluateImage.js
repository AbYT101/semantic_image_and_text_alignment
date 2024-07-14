import React, { useState } from 'react';
import { evaluateImage } from '../services/evaluateService';
import { toast } from 'react-hot-toast';

const EvaluateImage = () => {
  const [file, setFile] = useState(null);
  const [description, setDescription] = useState('');
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleEvaluate = () => {
    if (!file) {
      toast.error('Please select an image.');
      return;
    }

    evaluateImage(file, description).subscribe({
      next: (response) => {
        if (response.result) {
          toast.success('Image evaluated successfully!');
          setResult(response.result);
        } else {
          toast.error('Failed to evaluate image.');
        }
      },
      error: (error) => {
        toast.error('Error evaluating image!');
        console.error(error);
      }
    });
  };

  return (
    <div className="max-w-xl mx-auto p-6 bg-white shadow-md rounded-lg">
      <h2 className="text-2xl font-bold mb-6 text-gray-800">Evaluate Image</h2>
      <form className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-700">Upload Image</label>
          <input
            type="file"
            onChange={handleFileChange}
            className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Description</label>
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Description"
            className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm"
          />
        </div>
        <div>
          <button
            type="button"
            onClick={handleEvaluate}
            className="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
          >
            Evaluate
          </button>
        </div>
      </form>
      {result && (
        <div className="mt-6 p-4 bg-gray-100 border-l-4 border-green-600">
          <p className="text-sm text-gray-700">{result}</p>
        </div>
      )}
    </div>
  );
};

export default EvaluateImage;
