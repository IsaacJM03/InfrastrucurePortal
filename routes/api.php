<?php

use App\Http\Controllers\UserController;
use App\Http\Controllers\ApnRequestController;
use App\Http\Controllers\DeviceController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::post('/register', [UserController::class, 'register']);
Route::post('/login', [UserController::class, 'login']);

Route::middleware(['auth:api', 'role:superadmin|admin'])->group(function () {
    Route::get('/admin/users', [UserController::class, 'getAdminUsers']);
    Route::get('/devices', [DeviceController::class, 'index']);
    Route::post('/devices', [DeviceController::class, 'store']);
    Route::get('/devices/{id}', [DeviceController::class, 'show']);
    Route::put('/devices/{id}', [DeviceController::class, 'update']);
    Route::delete('/devices/{id}', [DeviceController::class, 'destroy']);
    Route::get('/apn-requests', [ApnRequestController::class, 'index']);
    Route::get('/apn-requests/{id}', [ApnRequestController::class, 'show']);
    Route::put('/apn-requests/{id}', [ApnRequestController::class, 'update']);
    Route::delete('/apn-requests/{id}', [ApnRequestController::class, 'destroy']);
});

Route::middleware(['auth:api', 'role:superadmin'])->group(function () {
    Route::post('/users/assign-role', [UserController::class, 'assignRole']);
});

Route::middleware('auth:api')->group(function () {
    Route::post('/apn-requests', [ApnRequestController::class, 'store']);
    Route::get('/user', [UserController::class, 'getUser']);
});