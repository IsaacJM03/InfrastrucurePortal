<?php

namespace App\Http\Controllers;

use App\Models\ApnRequest;
use Illuminate\Http\Request;

class ApnRequestController extends Controller
{
    public function index()
    {
        $apnRequests = ApnRequest::with('user')->get();
        return response()->json($apnRequests, 200);
    }

    public function store(Request $request)
    {
        $request->validate([
            'phone_number' => 'required|string',
            'ip_address' => 'required|ip',
        ]);

        $apnRequest = ApnRequest::create([
            'user_id' => auth()->id(),
            'phone_number' => $request->phone_number,
            'ip_address' => $request->ip_address,
            'date_requested' => now(),
        ]);

        return response()->json($apnRequest, 201);
    }

    public function show($id)
    {
        $apnRequest = ApnRequest::with('user')->find($id);
        
        if (!$apnRequest) {
            return response()->json(['message' => 'APN request not found'], 404);
        }

        return response()->json($apnRequest, 200);
    }

    public function update(Request $request, $id)
    {
        $apnRequest = ApnRequest::find($id);

        if (!$apnRequest) {
            return response()->json(['message' => 'APN request not found'], 404);
        }

        $request->validate([
            'status' => 'in:pending,approved,rejected',
            'admin_remarks' => 'string|nullable',
            'date_taken' => 'date|nullable',
            'date_returned' => 'date|nullable',
        ]);

        if ($request->status === 'approved' && !$apnRequest->date_taken) {
            $request->merge(['date_taken' => now()]);
        } elseif ($request->status === 'rejected') {
            $request->merge(['date_returned' => now()]);
        }

        $apnRequest->update($request->all());

        return response()->json($apnRequest, 200);
    }

    public function destroy($id)
    {
        $apnRequest = ApnRequest::find($id);

        if (!$apnRequest) {
            return response()->json(['message' => 'APN request not found'], 404);
        }

        $apnRequest->delete();

        return response()->json(['message' => 'APN request deleted'], 200);
    }
}
