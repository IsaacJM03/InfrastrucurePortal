<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ApnRequest extends Model
{
    use HasFactory;

    protected $fillable = [
        'user_id', 'phone_number', 'ip_address', 'date_requested', 'date_taken', 'date_returned', 'status', 'admin_remarks'
    ];

    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
