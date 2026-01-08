'use client';

import { useState } from 'react';
import Image from 'next/image';
import AuthModal from '@/components/auth-modal';
import { useAuth } from '@/contexts/auth-context';

export default function Home() {
  const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);
  const [authView, setAuthView] = useState<'login' | 'signup'>('login');
  const { user, loading } = useAuth();

  const openAuthModal = (view: 'login' | 'signup') => {
    setAuthView(view);
    setIsAuthModalOpen(true);
  };

  if (loading) {
    return <div className="flex items-center justify-center min-h-screen">Loading...</div>;
  }

  if (user) {
    // Redirect to dashboard if user is logged in
    typeof window !== 'undefined' && (window.location.href = '/dashboard');
    return null;
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start sm:text-left">
        {/* Navigation Bar */}
        <nav className="w-full flex justify-between items-center pb-8">
          <div className="text-2xl font-bold text-blue-600">TaskMastery</div>
          <div className="flex space-x-4">
            <a href="#" className="text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-200">AI Chat</a>
            <a href="#" className="text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-200">Dashboard</a>
            <button 
              onClick={() => openAuthModal('login')}
              className="text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-200"
            >
              Login
            </button>
            <button 
              onClick={() => openAuthModal('signup')}
              className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
            >
              Sign Up
            </button>
          </div>
        </nav>

        {/* Hero Section */}
        <div className="flex flex-col items-center gap-6 text-center sm:items-start sm:text-left">
          <h1 className="max-w-xs text-3xl font-semibold leading-10 tracking-tight text-black dark:text-zinc-50">
            <span className="text-blue-600">🚀</span> The Future of Productivity
          </h1>
          <h2 className="max-w-md text-xl text-zinc-600 dark:text-zinc-400">
            Transform Your Tasks Into Accomplishments
          </h2>
          <p className="max-w-md text-lg leading-8 text-zinc-600 dark:text-zinc-400">
            Harness the power of AI to organize, prioritize, and execute your tasks with precision. 
            Join thousands of professionals who have revolutionized their workflow.
          </p>
        </div>

        {/* CTA Buttons */}
        <div className="flex flex-col gap-4 text-base font-medium sm:flex-row mt-8">
          <button
            onClick={() => openAuthModal('signup')}
            className="flex h-12 w-full items-center justify-center gap-2 rounded-full bg-blue-600 text-white transition-colors hover:bg-blue-700 md:w-[158px]"
          >
            Get Started
          </button>
          <button
            onClick={() => openAuthModal('login')}
            className="flex h-12 w-full items-center justify-center rounded-full border border-solid border-black/[.08] transition-colors hover:border-transparent hover:bg-black/[.04] dark:border-white/[.145] dark:hover:bg-[#1a1a1a] md:w-[158px]"
          >
            Try AI Chat
          </button>
        </div>

        {/* Stats Section */}
        <div className="grid grid-cols-3 gap-8 mt-16 w-full">
          <div className="text-center">
            <div className="text-2xl font-bold text-blue-600">95%</div>
            <div className="text-gray-600 dark:text-gray-400">Task Completion</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-blue-600">4.8/5</div>
            <div className="text-gray-600 dark:text-gray-400">User Rating</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-blue-600">10K+</div>
            <div className="text-gray-600 dark:text-gray-400">Active Users</div>
          </div>
        </div>
      </main>

      {/* Auth Modal */}
      <AuthModal 
        isOpen={isAuthModalOpen} 
        onClose={() => setIsAuthModalOpen(false)} 
        initialView={authView}
      />
    </div>
  );
}