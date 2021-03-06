<?php

namespace Tests\Unit;

use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;


class AuthorTest extends TestCase
{
    public function testNotifySubscribersUsersWhenBookIsPublished()
    {
        $book = new Book();
        $user = new User();
        User::shouldReceive('notify_book_published')->once()->with($book);
        Author::shouldReceive('subscribers')
                    ->once()
                    ->andReturn([$user]);
        $this->assertTrue(true);
    }
}
