import axios from 'axios';
import { from, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

export const evaluateImage = (file, imageAnalyzer, description) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('imageAnalyzer', imageAnalyzer)
  formData.append('description', description);

  return from(
    axios.post('http://localhost:5000/evaluate', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    }).then(response => response.data)
  ).pipe(
    catchError(error => {
      console.error('Error evaluating image:', error);
      return throwError(error);
    })
  );
};
