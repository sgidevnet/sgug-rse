Name:           sgugpushdpopd
Version:        0.1
Release:        1%{?dist}
Summary:        Adds pushd and popd to sgug-rse

License:        GPL
Source0:        pushd 
Source1:        popd

BuildArch:      noarch



%description


%prep
cp -av %{SOURCE0} .
cp -av %{SOURCE1} .


#%build


%install
install -m 755 -p -D %{SOURCE0} $RPM_BUILD_ROOT/usr/sgug/bin/pushd
install -m 755 -p -D %{SOURCE0} $RPM_BUILD_ROOT/usr/sgug/bin/popd


%files
/usr/sgug/bin/pushd
/usr/sgug/bin/popd


%changelog
* Tue Sep 29 2021  Unxmaal <eric.e.dodd@gmail.com> - 0.1-1
- Initial build.
