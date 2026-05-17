import React from 'react';

export default function Teams() {
  return (
    <div className="space-y-6 p-8">
      <h1 className="text-3xl font-bold text-gray-900">Teams</h1>
      <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900">No teams yet</h3>
          <p className="text-gray-500 mt-2">Create or join a team to collaborate with others.</p>
        </div>
      </div>
    </div>
  );
}
