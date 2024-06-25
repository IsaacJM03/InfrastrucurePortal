<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Device;

class DeviceController extends Controller
{
    public function index()
    {
        return response()->json(Device::all(), 200);
    }

    public function store(Request $request)
    {
        $request->validate([
            'name' => 'required|string',
            'ip_address' => 'required|ip|unique:devices',
            'model' => 'required|string',
        ]);

        $device = Device::create($request->all());

        return response()->json($device, 201);
    }

    public function show($id)
    {
        $device = Device::find($id);
        
        if (!$device) {
            return response()->json(['message' => 'Device not found'], 404);
        }

        return response()->json($device, 200);
    }

    public function update(Request $request, $id)
    {
        $device = Device::find($id);

        if (!$device) {
            return response()->json(['message' => 'Device not found'], 404);
        }

        $request->validate([
            'name' => 'string',
            'ip_address' => 'ip|unique:devices,ip_address,' . $id,
            'model' => 'string',
        ]);

        $device->update($request->all());

        return response()->json($device, 200);
    }

    public function destroy($id)
    {
        $device = Device::find($id);

        if (!$device) {
            return response()->json(['message' => 'Device not found'], 404);
        }

        $device->delete();

        return response()->json(['message' => 'Device deleted'], 200);
    }
}
