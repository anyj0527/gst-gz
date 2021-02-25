%define gstpostfix	gstreamer-1.0
%define gstlibdir	%{_libdir}/%{gstpostfix}

Name:   gst-gz
Summary: gst-gz: GStreamer plugins for compress and decompress
Version: 1.0.0
Release: 1
Group: Applications/Multimedia
Packager: Yongjoo Ahn <yongjoo1.ahn@samsung.com>
License: LGPL-2.1
Source:     %{name}-%{version}.tar.gz
Source1001: %{name}.manifest

Requires: gstraemer >= 1.8.0
BuildRequires:	gstreamer-devel
BuildRequires:	gst-plugins-base-devel

%description
gst-gz provides GStreamer plugins in order to compress and decompress data with zlib

%prep
%setup -q
cp %{SOURCE1001} .

%build

%autogen
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{gstlibdir}
install -m 755 src/.libs/libgstgz.so %{buildroot}/%{gstlibdir}
install -m 755 src/.libs/libgstgz.a %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
install -m 644 src/*.h %{buildroot}/%{_includedir}

%clean

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%{gstlibdir}/*.so

%files devel
%manifest %{name}.manifest
%{_includedir}/*.h
%{_libdir}/*.a
