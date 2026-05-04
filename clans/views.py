from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClanForm
from .models import ClanMembership

@login_required
def create_clan(request):
    if request.method == 'POST':
        form = ClanForm(request.POST)
        if form.is_valid():
            clan = form.save(commit=False)
            clan.leader = request.user
            clan.save()

            # automatically add leader as member
            ClanMembership.objects.create(
                user=request.user,
                clan=clan,
                role='admin'
            )

            return redirect('home')
    else:
        form = ClanForm()

    return render(request, 'clans/create_clan.html', {'form': form})