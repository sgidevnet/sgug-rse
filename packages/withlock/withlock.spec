%global github_owner    poeml
%global github_name     withlock
%global github_commit   6ffda60e1c91c591ebab41e18a4c5f1e58980f4e

Name:           withlock
Version:        0.5
Release:        8%{?dist}
Summary:        Locking wrapper script

License:        ASL 2.0
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{version}.tar.gz
# Specify /usr/bin/python3 to ensure use of py3
Patch0:         withlock-0.5-python3.patch
BuildArch:      noarch
BuildRequires:  gzip
Requires:       python3

%description
withlock is a locking wrapper script to make sure that some program
isn't run more than once. It is ideal to prevent periodic jobs spawned
by cron from stacking up.

The locks created are valid only while the wrapper is running, and
thus will never require additional cleanup, even after a reboot. This
makes the wrapper safe and easy to use, and much better than
implementing half-hearted locking within scripts.

%prep
%autosetup -p1 -n %{github_name}-%{github_commit}

%build
# No build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m 0755 withlock %{buildroot}%{_bindir}
install -m 0644 withlock.1 %{buildroot}%{_mandir}/man1
gzip %{buildroot}%{_mandir}/man1/withlock.1

%files
%license LICENSE-2.0.txt
%doc README.md
%{_bindir}/withlock
%{_mandir}/man1/withlock.1*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5-2
- Rebuild for Python 3.6

* Fri May 20 2016 Adam Williamson <awilliam@redhat.com> - 0.5-1
- update to 0.5
- switch to python3
- package license, README and manpage

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Apr 22 2015 Adam Williamson <awilliam@redhat.com> - 0.3-1
- initial package
