import React, { useState } from "react";
import { evaluateImage } from "../services/evaluateService";
import { toast } from "react-hot-toast";
import { Oval } from 'react-loader-spinner'; // Import the loader

const EvaluateImage = () => {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [description, setDescription] = useState("");
  const [imageAnalyzer, setImageAnalyzer] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false); // Loading state

  const handleFileChange = (e) => {
    const uploadedFile = e.target.files[0];
    setFile(uploadedFile);
    if (uploadedFile) {
      setPreview(URL.createObjectURL(uploadedFile));
    }
  };

  const handleEvaluate = () => {
    if (!file) {
      toast.error("Please select an image.");
      return;
    }

    setLoading(true); // Start loading
    evaluateImage(file, imageAnalyzer, description).subscribe({
      next: (response) => {
        setLoading(false); // Stop loading
        if (response.result) {
          toast.success("Image evaluated successfully!");
          setResult(response.result);
        } else {
          toast.error("Failed to evaluate image.");
        }
      },
      error: (error) => {
        setLoading(false); // Stop loading
        toast.error("Error evaluating image!");
        console.error(error);
      },
    });
  };

  return (
    <div className="max-w-7xl mx-auto p-6 bg-white shadow-md rounded-lg flex space-x-6">
      <div className="flex-1">
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
          {preview && (
            <div className="mt-4 flex justify-center">
              <img
                src={preview}
                alt="Preview"
                className="max-w-full max-h-64 rounded-md shadow-sm"
              />
            </div>
          )}
          <div>
            <label className="block text-sm font-medium text-gray-700">Image/Text Analyzer</label>
            <select
              value={imageAnalyzer}
              onChange={(e) => setImageAnalyzer(e.target.value)}
              className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500 sm:text-sm"
            >
              <option value=''>Select Analyzer</option>
              <option value="YOLO + Tesseract">YOLO + Tesseract</option>
              <option value="OpenAI GPT-4o">OpenAI GPT-4o</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Concept</label>
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
      </div>
      <div className="flex-1 mt-6 p-6 bg-gray-100 border-l-4 border-green-600 shadow-md rounded-lg">
        {loading ? (
          <div className="flex justify-center items-center h-full">
            <Oval
              height={80}
              width={80}
              color="#4fa94d"
              wrapperStyle={{}}
              wrapperClass=""
              visible={true}
              ariaLabel="oval-loading"
              secondaryColor="#4fa94d"
              strokeWidth={2}
              strokeWidthSecondary={2}
            />
          </div>
        ) : (
          result && (
            <div>
              <h3 className="text-lg font-medium text-gray-800 mb-4">Evaluation Result</h3>
              <div className="prose prose-green">
                {result.split('\n').map((line, index) => (
                  <React.Fragment key={index}>
                    {line.trim() && (
                      <>
                        {line.startsWith('### ') ? (
                          <h3 className="font-medium text-gray-700 mb-2">
                            {line.replace('### ', '')}
                          </h3>
                        ) : line.startsWith('## ') ? (
                          <h2 className="font-semibold text-gray-800 mb-2">
                            {line.replace('## ', '')}
                          </h2>
                        ) : line.startsWith('# ') ? (
                          <h1 className="font-bold text-gray-900 mb-2">
                            {line.replace('# ', '')}
                          </h1>
                        ) : line.startsWith('**') && line.endsWith('**') ? (
                          <strong>{line.replace(/\*\*/g, '')}</strong>
                        ) : (
                          <p>{line}</p>
                        )}
                      </>
                    )}
                  </React.Fragment>
                ))}
              </div>
            </div>
          )
        )}
      </div>
    </div>
  );
};

export default EvaluateImage;
