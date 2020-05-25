from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from board.models import Board
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")


def board(request):
    rsBoard=Board.objects.all()

    return render(request, "board_list.html", {
        'rsBoard': rsBoard
    })


def board_write(request):
    return render(request, "board_write.html")


def board_insert(request):
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']
    bdate = timezone.now()

    if btitle != "":
        Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter, b_date=bdate)
        return redirect('/board_ajax')
    else:
        return redirect('/board_write')


def board_insert_ajax(request):
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']
    bdate = timezone.now()

    if btitle != "":
        Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter, b_date=bdate)
        return redirect('/board_ajax')
    else:
        return redirect('/board_write')


def board_view(request):
    bno = request.GET['b_no']
    rsData = Board.objects.get(b_no=bno)
    rsData.b_count += 1
    rsData.save()

    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_view.html", {
        'rsDetail': rsDetail
    })


def board_edit(request):
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_edit.html", {
        'rsDetail': rsDetail
    })


def board_update(request):
    bno = request.GET['b_no']
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']
    bdate = timezone.now()

    try:
        board = Board.objects.get(b_no=bno)
        if btitle != "":
            board.b_title = btitle
        if bnote != "":
            board.b_note = bnote
        if bwriter != "":
            board.b_writer = bwriter
        board.b_date = bdate

        try:
            board.save()
            return redirect('/board')
        except ValueError:
            return Response({"success": False, "msg": "에러입니다."})

    except ObjectDoesNotExist:
        return Response({"success": False, "msg": " 게시글 없음."})


def board_delete(request):
    bno = request.GET['b_no']
    Board.objects.get(b_no=bno).delete()

    return redirect('/board')


def board_ajax(request):
    rsBoard = Board.objects.all()

    return render(request, "board_ajax.html", {
        'rsBoard': rsBoard
    })


@csrf_exempt
def board_deleteajax(request):
    bno = request.GET['b_no']
    Board.objects.get(b_no=bno).delete()

    data={}
    data['result_msg'] = '삭제되었습니다.'

    return JsonResponse(data, content_type="application/json")


def portfolio(request):
    rsBoard = Board.objects.all()

    return render(request, "portfolio.html", {
        'rsBoard': rsBoard
    })


def portfolio_detail(request):
    rsBoard = Board.objects.all()

    return render(request, "portfolio_details.html", {
        'rsBoard': rsBoard
    })