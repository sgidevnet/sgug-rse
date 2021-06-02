%global srcname plaster
%global sum Application configuration settings abstraction layer
%global desc plaster is a loader interface around multiple \
configuration file formats. It exists to define a common API for \
applications to use when they wish to load configuration. The library \
itself does not aim to handle anything except a basic API that \
applications may use to find and load configuration settings. Any \
specific constraints should be implemented in a loader which can be \
registered via an entry point.


Name: python-%{srcname}
Version: 0.5
Release: 7%{?dist}
BuildArch: noarch

License: MIT
Summary: %{sum}
URL:     https://github.com/Pylons/%{srcname}
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: python2-devel
BuildRequires: python2-pytest
BuildRequires: python2-setuptools
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx


%description
%{desc}


%package doc
Summary: Documentation for %{name}


%description doc
Contains the documentation for %{name}.


%package -n python2-%{srcname}
Summary: %{sum}

Requires: python2-setuptools

%{?python_provide:%python_provide python2-%{srcname}}


%description -n python2-%{srcname}
%{desc}


%package -n python3-%{srcname}
Summary: %{sum}

Requires: python3-setuptools

%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}

# The plaster docs upstream only build if plaster is installed. Since we are building plaster docs
# from a source checkout, let's insert plaster into the path.
sed -i "s:import plaster:sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))\nimport plaster:" docs/conf.py

# Related to the above, upstream plaster gets the version for the docs by using pkg_resources which
# can only work if plaster is installed. Let's just substitute the version in since we know what it
# is.
sed -i "s/version = pkg_resources.*/version = '%{version}'/" docs/conf.py

# Upstream docs use pylons_sphinx_themes, which isn't packaged for Fedora yet. Let's just convert it
# to use the standard sphinx theme for now.
sed -i "/import pylons_sphinx_themes/d" docs/conf.py
sed -i "/html_theme_path =.*/d" docs/conf.py
sed -i "/html_theme =.*/d" docs/conf.py
sed -i "/.*github_url.*/d" docs/conf.py


%build
make %{?_smp_mflags} -C docs html
rm -rf docs/_build/html/.buildinfo

%py2_build
%py3_build


%install
%py2_install
%py3_install


%check
PYTHONPATH="./src" py.test-2
PYTHONPATH="./src" py.test-3


%files doc
%license LICENSE.txt
%doc docs/_build/html
%doc CHANGES.rst
%doc README.rst


%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/*.egg-info


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.5-1
- Initial release.
