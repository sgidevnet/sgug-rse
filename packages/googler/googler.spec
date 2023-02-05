Name:       googler
Version:    4.1
Release:    1%{?dist}
Summary:    Access google search, google site search, google news from the terminal

License:    GPLv3+
URL:        https://github.com/jarun/googler
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make


%description
googler is a power tool to access Google (Web & News) websites and Google Site
Search website from the command-line. It shows the title, URL and abstract
for each result, which can be directly opened in a browser from the terminal.
Results are fetched in pages (with page navigation). Supports sequential
searches in a single googler instance.

googler was initially written to cater to headless servers without X. You can
integrate it with a text-based browser. However, it has grown into a very handy
and flexible utility that delivers much more. For example, fetch any number of
results or start anywhere, limit search by any duration, define aliases to
google search any number of websites, switch domains easily... all of this
in a very clean interface without ads or stray URLs. The shell completion
scripts make sure you don't need to remember any options.

googler isn't affiliated to Google in any way.


%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '1s/env //' googler


%build
make disable-self-upgrade


%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/googler-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  auto-completion/fish/googler.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_googler


%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bash-completion/completions/googler-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/googler.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_googler


%changelog
* Fri Jun 19 23:28:58 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.1-1
- Release 4.1 (#1830152)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 21:54:30 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 4.0-1
- Release 4.0 (#1777084)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 14:45:36 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.9-1
- Release 3.9 (#1715305)

* Wed Mar 27 16:11:44 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.8-1
- Release 3.8 (#1693334)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.7.1-1
- Release 3.7.1

* Sun Sep 16 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.7-1
- Release 3.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.6-1
- Release 3.6

* Sat Feb 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.5-1
- First RPM release
