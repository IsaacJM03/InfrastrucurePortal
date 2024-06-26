<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;
use Illuminate\Support\Facades\Auth;

class RoleMiddleware
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     * $role
     */
    
     public function handle($request, Closure $next, string $role)
     {
        if (!Auth::check() || !$request->user()->hasRole($role)) {
            return response()->json(['error' => 'Unauthorized'], 403);
        }
 
         return $next($request);
     }
}
