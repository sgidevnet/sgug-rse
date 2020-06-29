%global srcname sphinxcontrib-trio

Name:           python-%{srcname}
Version:        1.1.2
Release:        2%{?dist}
Summary:        Make Sphinx better at documenting Python functions and methods
License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/sphinxcontrib-trio
Source0:        %{pypi_source}
BuildArch:      noarch

%global desc                                                            \
This sphinx extension helps you document Python code that uses          \
async/await, or abstract methods, or context managers, or generators,   \
or ... you get the idea. It works by making sphinx's regular            \
directives for documenting Python functions and methods smarter and     \
more powerful. The name is because it was originally written for the    \
Trio project, and I'm not very creative. But don't be put off –         \
there's nothing Trio- or async-specific about this extension; any       \
Python project can benefit. (Though projects using async/await          \
probably benefit the most, since sphinx's built-in tools are            \
especially inadequate in this case.)

%description
%desc


%package -n python3-%{srcname}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  %{_bindir}/rst2html
BuildRequires:  make
Summary: %{summary}

%description -n python3-%{srcname}
%desc


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build
make -C docs html SPHINXBUILD=%{_bindir}/sphinx-build-3
rm -f docs/build/html/.buildinfo
rst2html README.rst README.html

%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%doc README.rst README.html
%doc docs/build/html
%{python3_sitelib}/*


%changelog
* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-2
- Rebuilt for Python 3.9

* Wed May  6 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.2-1
- Update to 1.1.2.

* Fri Apr 10 2020 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.1-1
- Update to 1.1.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.0-1
- Update to 1.1.0.
- Build docs.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.2-1
- Update to 1.0.2.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.7

* Wed Apr 25 2018 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1-1
- New package.
