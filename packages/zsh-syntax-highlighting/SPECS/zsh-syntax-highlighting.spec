Name:    zsh-syntax-highlighting
Version: 0.7.1
Release: 1%{?dist}

Summary: Fish shell like syntax highlighting for Zsh
License: BSD
URL:     https://github.com/zsh-users/zsh-syntax-highlighting
Source0: https://github.com/zsh-users/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: zsh

Requires: zsh

%description
This package provides syntax highlighting for the shell zsh. It enables
highlighting of commands whilst they are typed at a zsh prompt into an
interactive terminal. This helps in reviewing commands before running them,
particularly in catching syntax errors.

%prep
%autosetup

%build
make

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
rm %{buildroot}/%{_docdir}/%{name}/COPYING.md

%check
#make test
#make perf

%files
%doc INSTALL.md
%license COPYING.md
%{_docdir}/%{name}
%{_datadir}/%{name}

%changelog
* Sat Feb 29 2020 Michael Kuhn <suraia@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 02 2017 Michael Kuhn <suraia@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Michael Kuhn <suraia@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Mon Aug 29 2016 Michael Kuhn <suraia@fedoraproject.org> - 0.4.1-1
- Initial package
