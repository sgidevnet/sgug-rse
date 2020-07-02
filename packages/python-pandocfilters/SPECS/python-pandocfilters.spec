Name:		python-pandocfilters
Version:	1.4.1
Release:	12%{?dist}
Summary:	Python module for writing pandoc filters

License:	BSD
URL:		https://github.com/jgm/pandocfilters
Source0:	https://files.pythonhosted.org/packages/source/p/pandocfilters/pandocfilters-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel

%global _docdir_fmt %{name}

%global _description \
This package provides a few utility functions which make it easier to\
write pandoc filters in Python.

%description %_description

%package -n python3-pandocfilters
Summary:	Python module for writing pandoc filters
%{?python_provide:%python_provide python3-pandocfilters}

%description -n python3-pandocfilters %_description

%prep
%autosetup -n pandocfilters-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-pandocfilters
%license LICENSE
%doc README
%doc examples/
%{python3_sitelib}/pandocfilters.py
%{python3_sitelib}/pandocfilters-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/__pycache__/*

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-6
- Subpackage python2-pandocfilters has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-1
- Updated to 1.4.1 (#1461274)
- Changed Source0 link to PyPI (GitHub tag is missing for this release)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-6
- Rebuild for Python 3.6

* Thu Nov 17 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-5
- Spec file modernization, fix ownership of __pycache__

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Jun 27 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-1
- Initial packaging (#1236328)
