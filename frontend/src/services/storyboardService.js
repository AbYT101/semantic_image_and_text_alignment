import axios from 'axios';
import { from } from 'rxjs';

export const synthesisStoryboard = (files, descriptions) => {
  const formData = new FormData();
  files.forEach(file => formData.append('files', file));
  descriptions.forEach(description => formData.append('descriptions', description));

  const response$ = from(
    axios.post('http://localhost:5000/synthesis-storyboard', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  );

  return response$;
};
