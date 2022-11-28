Name:       ddgr
Version:    1.7
Release:    1%{?dist}
Summary:    DuckDuckGo from the terminal

License:    GPLv3+
URL:        https://github.com/jarun/ddgr
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make
BuildRequires:  python3-devel


%description
ddgr is a cmdline utility to search DuckDuckGo from the terminal.
While googler is highly popular among cmdline users, in many forums the need
of a similar utility for privacy-aware DuckDuckGo came up. DuckDuckGo Bangs
are super-cool too! So here's ddgr for you!

Unlike the web interface, you can specify the number of search results you
would like to see per page. It's more convenient than skimming through
30-odd search results per page. The default interface is carefully
designed to use minimum space without sacrificing readability.

ddgr isn't affiliated to DuckDuckGo in any way.


%prep
%autosetup -p1 -n %{name}-%{version}
sed -i "s|\tinstall -|\t\$(INSTALL) -|" Makefile
sed -i '1s/env //' ddgr


%build
# Nothing to do


%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/ddgr-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  auto-completion/fish/ddgr.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_ddgr


%check
make test


%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bash-completion/completions/ddgr-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/ddgr.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_ddgr


%changelog
* Thu Sep 12 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.7-1
- Release 1.7

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.6-1
- Release 1.6

* Tue Sep 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.5-1
- Release 1.5

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4-2
- Rebuilt for Python 3.7

* Thu Apr 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-1
- Release 1.4

* Fri Jan 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.2-1
- First RPM release
