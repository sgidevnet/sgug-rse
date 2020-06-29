%global srcname pytaglib

Name:           python-%{srcname}
Version:        1.4.5
Release:        5%{?dist}
Summary:        Python audio metadata ("tagging") library based on TagLib

License:        GPLv3+
URL:            https://github.com/supermihi/pytaglib
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

Patch0001:      0001-Remove-unnecessary-py_modules-line-in-setup.py.patch
Patch0002:      0002-Fix-62-add-pyprinttags-to-py_modules.patch

BuildRequires:  gcc-c++
BuildRequires:  taglib-devel

%global _description \
pytaglib is a full-featured, easy-to-use, cross-platform audio metadata\
(“tag”) library for Python (all versions supported). It uses the popular,\
fast and rock-solid TagLib C++ library internally.\
\
pytaglib is a very thin wrapper about TagLib (<150 lines of code), meaning\
that you immediately profit from the underlying library’s speed and stability.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
# Remove pre-generated source
rm -vf src/taglib.cpp
# remove useless shebang
sed -i -e '1{\@^#!/usr/bin/env python@d}' src/pyprinttags.py

%build
%py3_build -- --cython

%install
%py3_install
# Not interested in having 2 binaries doing same thing
mv -f %{buildroot}%{_bindir}/pyprinttags{3,}

%check
%{__python3} setup.py ptr

%files -n python3-%{srcname}
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/pyprinttags
%{python3_sitearch}/%{srcname}-*.egg-info/
%{python3_sitearch}/taglib.*.so
%{python3_sitearch}/pyprinttags.py
%{python3_sitearch}/__pycache__/pyprinttags.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-2
- Rebuilt for Python 3.8

* Sun Aug 04 14:51:47 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.5-1
- Update to 1.4.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.3-4
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-2
- Rebuilt for Python 3.7

* Sun Mar 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Sat Sep 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-1
- Initial package
