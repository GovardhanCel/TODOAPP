import { useCallback, useEffect, useState } from 'react';
import axios from 'axios';

interface Todo {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  priority: string;
  dueDate?: string;
  createdAt: string;
}

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5500';

export default function Dashboard() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [priority, setPriority] = useState('MEDIUM');
  const [loading, setLoading] = useState(false);
  const [userId] = useState('demo-user'); // In production, get from auth context

  // Fetch todos on mount
  const fetchTodos = useCallback(async () => {
    try {
      const response = await axios.get(`${API_URL}/api/todos`, {
        params: { userId },
      });
      setTodos(response.data);
    } catch (error) {
      console.error('Failed to fetch todos:', error);
    }
  }, [userId]); // 👈 add actual dependencies

  useEffect(() => {
    fetchTodos();
  }, [fetchTodos]);

  const handleCreateTodo = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;

    setLoading(true);
    try {
      await axios.post(`${API_URL}/api/todos`, {
        title,
        description,
        priority,
        userId,
      });
      setTitle('');
      setDescription('');
      setPriority('MEDIUM');
      fetchTodos();
    } catch (error) {
      console.error('Failed to create todo:', error);
      alert('Failed to create todo');
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteTodo = async (id: string) => {
    if (!window.confirm('Are you sure you want to delete this todo?')) return;

    try {
      await axios.delete(`${API_URL}/api/todos/${id}`);
      fetchTodos();
    } catch (error) {
      console.error('Failed to delete todo:', error);
      alert('Failed to delete todo');
    }
  };

  const handleToggleTodo = async (todo: Todo) => {
    try {
      await axios.put(`${API_URL}/api/todos/${todo.id}`, {
        completed: !todo.completed,
      });
      fetchTodos();
    } catch (error) {
      console.error('Failed to update todo:', error);
    }
  };

  const activeTodos = todos.filter((t) => !t.completed);
  const completedTodos = todos.filter((t) => t.completed);
  const overdueTodos = todos.filter(
    (t) =>
      !t.completed &&
      t.dueDate &&
      new Date(t.dueDate) < new Date()
  );

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-white shadow">
        <div className="p-6">
          <h1 className="text-2xl font-bold text-gray-900">TODO App</h1>
        </div>
        <nav className="mt-6">
          <a href="/" className="block px-6 py-2 text-gray-700 hover:bg-gray-100 bg-gray-100">
            My Tasks
          </a>
          <a href="/teams" className="block px-6 py-2 text-gray-700 hover:bg-gray-100">
            Teams
          </a>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-auto">
        <div className="p-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-8">My Tasks</h2>

          {/* Stats */}
          <div className="grid grid-cols-1 gap-6 md:grid-cols-3 mb-8">
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-semibold text-gray-900">Active Tasks</h3>
              <p className="text-3xl font-bold text-blue-600 mt-2">{activeTodos.length}</p>
            </div>
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-semibold text-gray-900">Completed</h3>
              <p className="text-3xl font-bold text-green-600 mt-2">{completedTodos.length}</p>
            </div>
            <div className="bg-white rounded-lg shadow p-6">
              <h3 className="text-lg font-semibold text-gray-900">Overdue</h3>
              <p className="text-3xl font-bold text-red-600 mt-2">{overdueTodos.length}</p>
            </div>
          </div>

          {/* Create Todo Form */}
          <div className="bg-white rounded-lg shadow p-6 mb-8">
            <h3 className="text-xl font-semibold text-gray-900 mb-4">Create New Task</h3>
            <form onSubmit={handleCreateTodo} className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Task Title *
                </label>
                <input
                  type="text"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  placeholder="Enter task title"
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Description
                </label>
                <textarea
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  placeholder="Enter task description"
                  rows={3}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div className="flex gap-4">
                <div className="flex-1">
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Priority
                  </label>
                  <select
                    value={priority}
                    onChange={(e) => setPriority(e.target.value)}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                  >
                    <option value="LOW">Low</option>
                    <option value="MEDIUM">Medium</option>
                    <option value="HIGH">High</option>
                  </select>
                </div>
                <div className="flex-1">
                  <button
                    type="submit"
                    disabled={loading}
                    className="mt-6 w-full bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:bg-gray-400"
                  >
                    {loading ? 'Creating...' : 'Create Task'}
                  </button>
                </div>
              </div>
            </form>
          </div>

          {/* Todo List */}
          <div className="bg-white rounded-lg shadow">
            <div className="p-6">
              <h3 className="text-xl font-semibold text-gray-900 mb-4">Tasks</h3>
              {todos.length === 0 ? (
                <p className="text-gray-500">No tasks yet. Create one to get started!</p>
              ) : (
                <div className="space-y-3">
                  {todos.map((todo) => (
                    <div
                      key={todo.id}
                      className={`p-4 border rounded-lg flex items-center justify-between ${
                        todo.completed
                          ? 'bg-gray-50 border-gray-200'
                          : 'bg-white border-gray-300'
                      }`}
                    >
                      <div className="flex items-center gap-3 flex-1">
                        <input
                          type="checkbox"
                          checked={todo.completed}
                          onChange={() => handleToggleTodo(todo)}
                          className="w-5 h-5 text-blue-600 rounded focus:ring-2 focus:ring-blue-500"
                        />
                        <div className="flex-1">
                          <p
                            className={`text-sm font-medium ${
                              todo.completed
                                ? 'line-through text-gray-500'
                                : 'text-gray-900'
                            }`}
                          >
                            {todo.title}
                          </p>
                          {todo.description && (
                            <p className="text-xs text-gray-500 mt-1">
                              {todo.description}
                            </p>
                          )}
                        </div>
                        <span
                          className={`text-xs px-2 py-1 rounded ${
                            todo.priority === 'HIGH'
                              ? 'bg-red-100 text-red-700'
                              : todo.priority === 'MEDIUM'
                              ? 'bg-yellow-100 text-yellow-700'
                              : 'bg-green-100 text-green-700'
                          }`}
                        >
                          {todo.priority}
                        </span>
                      </div>
                      <button
                        onClick={() => handleDeleteTodo(todo.id)}
                        className="ml-4 px-3 py-1 text-sm text-red-600 hover:bg-red-50 rounded"
                      >
                        Delete
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
