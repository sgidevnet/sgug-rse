Name:           python-sphinxcontrib-github-alt
Version:        1.2
Release:        1%{?dist}
Summary:        Link to GitHub issues, pull requests, commits and users from Sphinx docs
License:        BSD
URL:            https://github.com/jupyter/sphinxcontrib_github_alt
Source0:        %pypi_source sphinxcontrib_github_alt

BuildArch:      noarch

BuildRequires:  python3-pip
BuildRequires:  python3-devel
BuildRequires:  python3-flit
# for flit to analyze the README:
BuildRequires:  python3-pygments

%global _description \
Link to GitHub issues, pull requests, commits and users for a particular \
project. \
It's called 'alt' because sphinxcontrib-github already exists. IPython & \
Jupyter projects have been using the syntax defined in this extension for \
some time before we made it into its own package, so we didn't want to \
switch to sphinxcontrib-github.

%description %_description


%package -n     python3-sphinxcontrib-github-alt
Summary:        %summary
Provides:       python3-sphinxcontrib_github_alt = %{version}-%{release}
%{?python_provide:%python_provide python3-sphinxcontrib-github-alt}
%{?python_provide:%python_provide python3-sphinxcontrib_github_alt}

%description -n python3-sphinxcontrib-github-alt

%_description


%prep
%autosetup -n sphinxcontrib_github_alt-%{version}


%build
# this package has no setup.py, it uses flit
export FLIT_NO_NETWORK=1
flit build --format wheel


%install
# We install the wheel created at %%build
%py3_install_wheel sphinxcontrib_github_alt-%{version}-py2.py3-none-any.whl 


# no tests, no %%check


%files -n python3-sphinxcontrib-github-alt
%doc README.rst
%license COPYING.md
%{python3_sitelib}/sphinxcontrib_github_alt-%{version}.dist-info/
%{python3_sitelib}/sphinxcontrib_github_alt.py
%{python3_sitelib}/__pycache__/sphinxcontrib_github_alt*


%changelog
* Mon Jun 1 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.2-1
- Update to 1.2 (#1828203)

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-1
- initial package
