%global srcname Markdown
%global pkgname markdown

Name:           python-%{pkgname}
Version:        3.1.1
Release:        5%{?dist}
Summary:        Markdown implementation in Python
License:        BSD
URL:            https://python-markdown.github.io/
Source0:        https://files.pythonhosted.org/packages/source/M/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a Python implementation of John Gruber’s Markdown. It is
almost completely compliant with the reference implementation, though
there are a few very minor differences.


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        Markdown implementation in Python
BuildRequires:  python%{python3_pkgversion}-devel
#BuildRequires:  python%{python3_pkgversion}-PyYAML
#BuildRequires:  python%{python3_pkgversion}-tidy
Conflicts:      python2-%{pkgname} < 3.1-2
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description -n python%{python3_pkgversion}-%{pkgname}
This is a Python implementation of John Gruber''s Markdown. It is
almost completely compliant with the reference implementation, though
there are a few known issues.


%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build


%install
%py3_install

# process license file
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  %{buildroot}%{_bindir}/markdown_py \
  LICENSE.md > LICENSE.html


%check
%{__python3} ./setup.py test


%files -n python%{python3_pkgversion}-%{pkgname}
# temporarily skip packaging docs - see also
# https://github.com/Python-Markdown/markdown/issues/621
#doc python3/build/docs/*
%license LICENSE.*
%{python3_sitelib}/*
%{_bindir}/markdown_py


%changelog
* Mon Jun 15 2020 Daniel Hams <daniel.hams@gmail.com> - 3.1.1-5
- Rebuild with "newer" python3 package

* Mon May 1 2020 HAL <hal@null.not> - 1.16.0-6
- python3-markdown that builds on Irix 6.5

* Tue Aug 13 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.1.1-4
- Drop versioned binaries.

* Tue Aug 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1-3
- Drop Python 2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.1.1-1
- Update to 3.1.1.

* Fri May 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1-2
- Move /usr/bin/markdown_py to python3-markdown (#1705777)

* Tue Mar 26 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.1-1
- Update to 3.1.

* Mon Mar 25 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.1-1
- Update to 3.0.1.
- Simplify spec file.
- CLI tool uses Python3 now.
- Update BRs.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
