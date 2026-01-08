'use client';

import { useState, useEffect } from 'react';
import { useAuth } from '@/contexts/auth-context';
import { useRouter } from 'next/navigation';

// Define TypeScript interfaces
interface Todo {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
  user_id: string;
}

export default function Dashboard() {
  const { user, logout, loading } = useAuth();
  const router = useRouter();
  const [todos, setTodos] = useState<Todo[]>([]);
  const [filteredTodos, setFilteredTodos] = useState<Todo[]>([]);
  const [filter, setFilter] = useState<'all' | 'pending' | 'completed'>('all');
  const [newTodo, setNewTodo] = useState({ title: '', description: '' });
  const [loadingTodos, setLoadingTodos] = useState(true);
  const [error, setError] = useState('');

  // Fetch todos when component mounts or filter changes
  useEffect(() => {
    if (!user) return; // Don't fetch if not logged in
    
    const fetchTodos = async () => {
      try {
        setLoadingTodos(true);
        const response = await fetch('/api/v1/todos', {
          credentials: 'include',
        });
        
        if (!response.ok) {
          throw new Error('Failed to fetch todos');
        }
        
        const data = await response.json();
        setTodos(data);
      } catch (err) {
        setError('Failed to load todos');
        console.error(err);
      } finally {
        setLoadingTodos(false);
      }
    };

    fetchTodos();
  }, [user]);

  // Apply filter whenever todos or filter changes
  useEffect(() => {
    switch (filter) {
      case 'completed':
        setFilteredTodos(todos.filter(todo => todo.completed));
        break;
      case 'pending':
        setFilteredTodos(todos.filter(todo => !todo.completed));
        break;
      default:
        setFilteredTodos(todos);
    }
  }, [todos, filter]);

  const handleAddTodo = async (e: React.FormEvent) => {
    e.preventDefault();
    
    try {
      const response = await fetch('/api/v1/todos/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: newTodo.title,
          description: newTodo.description,
        }),
        credentials: 'include',
      });
      
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to add todo');
      }
      
      const createdTodo = await response.json();
      setTodos([...todos, createdTodo]);
      setNewTodo({ title: '', description: '' });
      setError('');
    } catch (err: any) {
      setError(err.message || 'Failed to add todo');
    }
  };

  const toggleTodo = async (id: string) => {
    const todo = todos.find(t => t.id === id);
    if (!todo) return;
    
    try {
      const response = await fetch(`/api/v1/todos/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          completed: !todo.completed,
        }),
        credentials: 'include',
      });
      
      if (!response.ok) {
        throw new Error('Failed to update todo');
      }
      
      const updatedTodo = await response.json();
      setTodos(todos.map(t => t.id === id ? updatedTodo : t));
    } catch (err) {
      setError('Failed to update todo');
      console.error(err);
    }
  };

  const deleteTodo = async (id: string) => {
    try {
      const response = await fetch(`/api/v1/todos/${id}`, {
        method: 'DELETE',
        credentials: 'include',
      });
      
      if (!response.ok) {
        throw new Error('Failed to delete todo');
      }
      
      setTodos(todos.filter(todo => todo.id !== id));
    } catch (err) {
      setError('Failed to delete todo');
      console.error(err);
    }
  };

  const handleLogout = async () => {
    try {
      await logout();
      router.push('/');
    } catch (err) {
      console.error('Logout error:', err);
    }
  };

  if (loading) {
    return <div className="flex items-center justify-center min-h-screen">Loading...</div>;
  }

  if (!user) {
    router.push('/');
    return null;
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      {/* Header */}
      <header className="bg-white dark:bg-gray-800 shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <h1 className="text-xl font-semibold text-gray-900 dark:text-white">TaskMastery Dashboard</h1>
            </div>
            <div className="flex items-center space-x-4">
              <span className="text-gray-700 dark:text-gray-300">Welcome, {user.name}</span>
              <button
                onClick={handleLogout}
                className="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
          {/* Left Sidebar */}
          <div className="lg:col-span-1">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
              <h2 className="text-lg font-medium text-gray-900 dark:text-white mb-4">Navigation</h2>
              <ul className="space-y-2">
                <li>
                  <a href="#" className="flex items-center justify-between text-blue-600 font-medium">
                    Dashboard
                    <span className="bg-blue-100 text-blue-800 text-xs font-medium px-2 py-0.5 rounded-full">
                      {todos.length}
                    </span>
                  </a>
                </li>
                <li>
                  <a href="#" className="flex items-center justify-between text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white">
                    My Tasks
                    <span className="bg-gray-100 text-gray-800 text-xs font-medium px-2 py-0.5 rounded-full dark:bg-gray-700 dark:text-gray-300">
                      {todos.filter(t => !t.completed).length}
                    </span>
                  </a>
                </li>
                <li>
                  <a href="#" className="flex items-center justify-between text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white">
                    Completed Tasks
                    <span className="bg-gray-100 text-gray-800 text-xs font-medium px-2 py-0.5 rounded-full dark:bg-gray-700 dark:text-gray-300">
                      {todos.filter(t => t.completed).length}
                    </span>
                  </a>
                </li>
                <li>
                  <button 
                    onClick={handleLogout}
                    className="text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white w-full text-left"
                  >
                    Logout
                  </button>
                </li>
              </ul>
            </div>
          </div>

          {/* Main Content Area */}
          <div className="lg:col-span-2">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow">
              {/* Add Todo Form */}
              <div className="p-6 border-b border-gray-200 dark:border-gray-700">
                <h2 className="text-lg font-medium text-gray-900 dark:text-white mb-4">Add New Task</h2>
                <form onSubmit={handleAddTodo}>
                  <div className="mb-4">
                    <input
                      type="text"
                      value={newTodo.title}
                      onChange={(e) => setNewTodo({...newTodo, title: e.target.value})}
                      placeholder="Task title"
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                      required
                    />
                  </div>
                  <div className="mb-4">
                    <textarea
                      value={newTodo.description}
                      onChange={(e) => setNewTodo({...newTodo, description: e.target.value})}
                      placeholder="Task description (optional)"
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                      rows={2}
                    />
                  </div>
                  <button
                    type="submit"
                    className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  >
                    Add Task
                  </button>
                </form>
              </div>

              {/* Filter Controls */}
              <div className="p-4 border-b border-gray-200 dark:border-gray-700 flex space-x-4">
                <button
                  onClick={() => setFilter('all')}
                  className={`px-4 py-2 rounded-md ${
                    filter === 'all'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600'
                  }`}
                >
                  All
                </button>
                <button
                  onClick={() => setFilter('pending')}
                  className={`px-4 py-2 rounded-md ${
                    filter === 'pending'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600'
                  }`}
                >
                  Pending
                </button>
                <button
                  onClick={() => setFilter('completed')}
                  className={`px-4 py-2 rounded-md ${
                    filter === 'completed'
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600'
                  }`}
                >
                  Completed
                </button>
              </div>

              {/* Todo List */}
              <div className="p-6">
                {error && (
                  <div className="mb-4 p-2 bg-red-100 text-red-700 rounded">
                    {error}
                  </div>
                )}

                {loadingTodos ? (
                  <div className="text-center py-4">Loading todos...</div>
                ) : filteredTodos.length === 0 ? (
                  <div className="text-center py-4 text-gray-500 dark:text-gray-400">
                    {filter === 'all' 
                      ? 'No tasks yet. Add your first task!' 
                      : filter === 'pending' 
                        ? 'No pending tasks. Great job!' 
                        : 'No completed tasks yet.'}
                  </div>
                ) : (
                  <ul className="space-y-4">
                    {filteredTodos.map((todo) => (
                      <li 
                        key={todo.id} 
                        className={`p-4 rounded-md border ${
                          todo.completed 
                            ? 'bg-green-50 border-green-200 dark:bg-green-900/20 dark:border-green-800' 
                            : 'bg-white border-gray-200 dark:bg-gray-700 dark:border-gray-600'
                        }`}
                      >
                        <div className="flex items-start">
                          <input
                            type="checkbox"
                            checked={todo.completed}
                            onChange={() => toggleTodo(todo.id)}
                            className="mt-1 h-5 w-5 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                          />
                          <div className="ml-3 flex-1">
                            <h3 
                              className={`text-lg ${
                                todo.completed 
                                  ? 'line-through text-gray-500 dark:text-gray-400' 
                                  : 'text-gray-900 dark:text-white'
                              }`}
                            >
                              {todo.title}
                            </h3>
                            {todo.description && (
                              <p className={`mt-1 ${
                                todo.completed 
                                  ? 'line-through text-gray-500 dark:text-gray-400' 
                                  : 'text-gray-600 dark:text-gray-300'
                              }`}>
                                {todo.description}
                              </p>
                            )}
                            <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
                              Created: {new Date(todo.created_at).toLocaleString()}
                            </p>
                          </div>
                          <button
                            onClick={() => deleteTodo(todo.id)}
                            className="ml-4 text-red-600 hover:text-red-800 dark:text-red-500 dark:hover:text-red-400"
                          >
                            Delete
                          </button>
                        </div>
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            </div>
          </div>

          {/* Right Panel - AI Chat (Placeholder) */}
          <div className="lg:col-span-1">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow h-full">
              <div className="p-4 border-b border-gray-200 dark:border-gray-700">
                <h2 className="text-lg font-medium text-gray-900 dark:text-white">AI Assistant</h2>
              </div>
              <div className="p-4 h-[calc(100%-56px)] flex flex-col">
                <div className="flex-1 overflow-y-auto mb-4 space-y-4">
                  <div className="bg-gray-100 dark:bg-gray-700 p-3 rounded-lg">
                    <p className="text-gray-800 dark:text-gray-200">Hello! I'm your AI assistant. How can I help you organize your tasks today?</p>
                  </div>
                  <div className="bg-blue-100 dark:bg-blue-900/30 p-3 rounded-lg ml-auto max-w-[80%]">
                    <p className="text-gray-800 dark:text-gray-200">Can you help me prioritize my tasks?</p>
                  </div>
                  <div className="bg-gray-100 dark:bg-gray-700 p-3 rounded-lg">
                    <p className="text-gray-800 dark:text-gray-200">Sure! Based on your deadlines and importance, I recommend focusing on high-priority tasks first.</p>
                  </div>
                </div>
                <div className="flex">
                  <input
                    type="text"
                    placeholder="Ask AI assistant..."
                    className="flex-1 px-3 py-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                  />
                  <button className="bg-blue-600 text-white px-4 py-2 rounded-r-md hover:bg-blue-700">
                    Send
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}