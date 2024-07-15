import React, { useState } from "react";
import { composeImage } from "../services/composeService";
import { toast } from "react-hot-toast";

const ComposeImage = () => {
  const [logo, setLogo] = useState(null);
  const [mainCharacter, setMainCharacter] = useState(null);
  const [background, setBackground] = useState(null);
  const [cta, setCta] = useState(null);
  const [result, setResult] = useState(null);
  const [descriptions, setDescriptions] = useState(null);

  const handleFileChange = (e, setter) => {
    setter(e.target.files[0]);
  };

  const handleCompose = async () => {
    // Validate all files are selected
    if (!logo || !mainCharacter || !background || !cta) {
      toast.error("Please upload all files.");
      return;
    }

    const files = [logo, mainCharacter, background, cta];
    try {
      const imageResults = await composeImage(files, descriptions);
      setResult(imageResults);
      toast.success("Images composed successfully!");
    } catch (error) {
      console.error("Error composing images:", error);
    }
  };

  return (
    <div className="max-w-xl mx-auto p-6 bg-white shadow-md rounded-lg">
      <h2 className="text-2xl font-bold mb-6 text-gray-800">Compose Image</h2>
      <form className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Upload Logo
          </label>
          <input
            type="file"
            onChange={(e) => handleFileChange(e, setLogo)}
            className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Upload Main Character
          </label>
          <input
            type="file"
            onChange={(e) => handleFileChange(e, setMainCharacter)}
            className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Upload Background
          </label>
          <input
            type="file"
            onChange={(e) => handleFileChange(e, setBackground)}
            className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Upload CTA
          </label>
          <input
            type="file"
            onChange={(e) => handleFileChange(e, setCta)}
            className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Description
          </label>
          <textarea
            value={descriptions}
            onChange={(e) => setDescriptions(e.target.value)}
            placeholder="Description"
            className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm"
          />
        </div>
        <div>
          <button
            type="button"
            onClick={handleCompose}
            className="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
          >
            Compose
          </button>
        </div>
      </form>
      {result && (
        <div className="mt-6 p-4 bg-gray-100 border-l-4 border-green-600">
          <img src={result} alt="Composed" className="w-full h-auto" />
        </div>
      )}
    </div>
  );
};

export default ComposeImage;
