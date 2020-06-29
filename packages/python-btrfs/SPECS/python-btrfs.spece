%global _description\
The primary goal of this module is to be able to inspect the internals of an\
existing filesystem for educational purposes.\
\
The python module acts as a wrapper around the low level kernel calls and btrfs\
data structures, presenting them as python objects with interesting attributes\
and references to other objects.

Name:           python-btrfs
Version:        11
Release:        6%{?dist}
Summary:        Python module to inspect btrfs filesystems
License:        LGPLv3+ and MIT
URL:            https://github.com/knorrie/python-btrfs
Source0:        https://github.com/knorrie/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

%description %_description

%package -n python3-btrfs
Summary: %{summary}
%{?python_provide:%python_provide python3-btrfs}
Suggests: %{name}-doc

%description -n python3-btrfs %_description

%package doc
Summary: %{summary}

%description doc %_description

%prep
%autosetup
# Remove dangling symlink
rm -f examples/btrfs
# Don't pull additional dependencies in doc
find examples -type f -print0 | xargs -0 chmod 644

%build
%py3_build
pushd docs
%make_build html
%make_build text
find build -name .buildinfo -delete
popd

%install
%py3_install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 bin/btrfs-balance-least-used %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-orphan-cleaner-progress %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-space-calculator %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-usage-report %{buildroot}%{_bindir}
install -m 0644 man/* %{buildroot}%{_mandir}/man1

%files -n python3-btrfs
%license COPYING.LESSER
%{python3_sitelib}/btrfs
%{python3_sitelib}/btrfs-%{version}-py*.egg-info
%{_bindir}/*
%{_mandir}/man1/*

%files doc
%doc CHANGES README.md examples
%doc docs/build/html docs/build/text
%license COPYING.LESSER

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 11-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 11-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 11-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 11-1
- Version 11

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 10-1
- Version 10
- License changed to LGPLv3+

* Tue Oct 23 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 9.1-2
- Suggests: python-btrfs-doc

* Mon Oct 22 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 9.1-1
- Version 9.1

* Mon Oct 22 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 9-1
- Version 9
- Create doc subpackage
- Use python_provide macro

* Fri Oct 12 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 8-6
- Add patch to support Python3.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 8-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 8-1
- Version 8

* Mon May 29 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 7-1
- Version 7

* Thu Mar 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 6-1
- Version 6
- Drop python2 subpackage

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 5-1
- Version 5

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 4-1
- Version 4

* Wed Nov 16 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.3-1
- Version 0.3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.2.1-2
- Remove doc subpackage

* Wed Jul 13 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.2.1-1
- Initial package
