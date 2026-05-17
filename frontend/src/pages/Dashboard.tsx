import React from 'react';

export default function Dashboard() {
  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-white shadow">
        <div className="p-6">
          <h1 className="text-2xl font-bold text-gray-900">TODO App</h1>
        </div>
        <nav className="mt-6">
          <a href="/" className="block px-6 py-2 text-gray-700 hover:bg-gray-100">
            My Tasks
          </a>
          <a href="/teams" className="block px-6 py-2 text-gray-700 hover:bg-gray-100">
            Teams
          </a>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-8">
        <h2 className="text-3xl font-bold text-gray-900 mb-8">My Tasks</h2>
        <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-semibold text-gray-900">Active Tasks</h3>
            <p className="text-3xl font-bold text-blue-600 mt-2">0</p>
          </div>
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-semibold text-gray-900">Completed</h3>
            <p className="text-3xl font-bold text-green-600 mt-2">0</p>
          </div>
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-semibold text-gray-900">Overdue</h3>
            <p className="text-3xl font-bold text-red-600 mt-2">0</p>
          </div>
        </div>

        {/* TODO List */}
        <div className="mt-8 bg-white rounded-lg shadow">
          <div className="p-6">
            <h3 className="text-xl font-semibold text-gray-900">Tasks</h3>
            <p className="text-gray-500 mt-4">No tasks yet. Create one to get started!</p>
          </div>
        </div>
      </main>
    </div>
  );
}
