import { NextRequest, NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
  // Check if the route is protected
  const isProtectedRoute = request.nextUrl.pathname.startsWith('/dashboard');
  
  if (isProtectedRoute) {
    // Check if user is authenticated by looking for auth token in cookies
    const authToken = request.cookies.get('auth_token'); // Adjust cookie name as needed
    
    if (!authToken) {
      // Redirect to login page if not authenticated
      return NextResponse.redirect(new URL('/', request.url));
    }
  }
  
  return NextResponse.next();
}

// Specify which paths the middleware should run for
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     */
    '/((?!api|_next/static|_next/image|favicon.ico).*)',
    '/dashboard/:path*',  // Protect dashboard routes
  ],
};